#!/usr/bin/env python3
"""Render a two-host Korean podcast script as a car-friendly MP3.

Requires: pip install edge-tts pydub ; ffmpeg on PATH.
This uses the unofficial edge-tts interface to an online speech service.
It is not a guaranteed/official API; retry and review the output before publishing.
"""
from __future__ import annotations

import argparse
import asyncio
import re
import tempfile
from pathlib import Path

import edge_tts
from pydub import AudioSegment

SPEAKERS = {
    "지훈": "ko-KR-InJoonNeural",
    "수아": "ko-KR-SunHiNeural",
}
TURN_RE = re.compile(r"^\*\*(지훈|수아):\*\*\s*(.+)$")
MARKDOWN_RE = re.compile(r"\*\*|\*|\x60")
LINK_RE = re.compile(r"\[([^]]+)\]\([^)]+\)")


def extract_turns(text: str) -> list[tuple[str, str, bool]]:
    turns = []
    new_section = False
    in_script = False
    for line in text.splitlines():
        if line.strip() == "---" and not in_script:
            in_script = True
            continue
        if not in_script:
            continue
        if line.startswith("## 음성 제작 가이드"):
            break
        if line.startswith("## "):
            new_section = True
            continue
        match = TURN_RE.match(line.strip())
        if not match:
            continue
        speaker, spoken = match.groups()
        spoken = LINK_RE.sub(r"\1", spoken)
        spoken = MARKDOWN_RE.sub("", spoken)
        spoken = spoken.replace("GEX", "지엑스").replace("Heatseeker", "히트시커")
        if spoken.strip():
            turns.append((speaker, spoken.strip(), new_section))
            new_section = False
    if not turns:
        raise ValueError("No speaker dialogue found in script")
    return turns


async def synthesize(speaker: str, text: str, path: Path, rate: str) -> None:
    for attempt in range(3):
        try:
            client = edge_tts.Communicate(text, SPEAKERS[speaker], rate=rate)
            await client.save(str(path))
            if path.stat().st_size <= 500:
                raise RuntimeError("TTS service returned an empty output")
            return
        except Exception:
            if attempt == 2:
                raise
            await asyncio.sleep(2 * (attempt + 1))


async def render(source: Path, destination: Path, max_turns: int, rate: str) -> None:
    turns = extract_turns(source.read_text(encoding="utf-8"))
    if max_turns:
        turns = turns[:max_turns]

    print(f"Rendering {len(turns)} dialogue turns from {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        audio = AudioSegment.silent(duration=700)
        # Serial synthesis avoids excess requests to the unofficial provider.
        for index, (speaker, spoken, section_start) in enumerate(turns, 1):
            file = folder / f"{index:04d}.mp3"
            await synthesize(speaker, spoken, file, rate)
            segment = AudioSegment.from_file(file, format="mp3").set_channels(1)
            # Balance alternating voices without squeezing their dynamic range.
            if segment.dBFS != float("-inf"):
                gain = min(7.0, max(-7.0, -20.0 - segment.dBFS))
                segment = segment.apply_gain(gain)
            audio += AudioSegment.silent(duration=850 if section_start else 340)
            audio += segment
            print(f"{index:03d}/{len(turns)} {speaker}: {len(spoken)} chars")
        audio += AudioSegment.silent(duration=1000)
        # Playback volume is intentionally comfortable rather than extremely loud.
        audio = audio.set_frame_rate(44100)
        if audio.max_dBFS > -1.5:
            audio = audio.apply_gain(-1.5 - audio.max_dBFS)
        audio.export(
            destination,
            format="mp3",
            bitrate="112k",
            tags={
                "title": "차트가 먼저다 — 감마의 브레이크와 가속 페달",
                "artist": "option101 오디오 클래스",
                "album": "option101 오디오 클래스",
                "track": "1",
                "language": "kor",
            },
        )
        print(f"Saved {destination} ({len(audio)/1000:.1f}s, {destination.stat().st_size} bytes)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="podcast/EP01-charts-and-gamma.md")
    parser.add_argument("--output", default="docs/public/podcast/ep01.mp3")
    parser.add_argument("--max-turns", type=int, default=0, help="For a short test render")
    parser.add_argument("--rate", default="-6%", help="Edge TTS speaking rate")
    args = parser.parse_args()
    asyncio.run(render(Path(args.input), Path(args.output), args.max_turns, args.rate))


if __name__ == "__main__":
    main()
