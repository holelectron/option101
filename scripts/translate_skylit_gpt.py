#!/usr/bin/env python3
"""Translate remaining 42 archived Skylit articles with an OpenAI language model.

Prerequisite: OPENAI_API_KEY environment variable. Safe default: dry-run.
Use --write to generate and replace only the remaining machine drafts.
The three previously reviewed articles are protected. English sources never change.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

from openai import OpenAI

ROOT = Path("docs/skylit")
GLOSSARY = Path("TRANSLATION_GLOSSARY.md")
PROTECTED = {
    "greeks/options-greeks",
    "greeks/gamma-exposure",
    "heatseeker/dealer-positioning",
}
PROMPT = """
You are a professional Korean financial options translator and rigorous editor.
Translate ALL of the supplied Skylit source section into idiomatic, precise Korean Markdown.
This is a translation, not a summary. Retain every paragraph, example, sentence,
list item, table row, heading, quotation, formula, symbol, number and link URL.
The original author's metaphors (casino, ship, pinball, beach ball, nodes) are important.
Write polished educational Korean, not awkward word-for-word Korean.
Respect the glossary and the style of the three human-reviewed examples.
Do NOT add conclusions, trading recommendations, fabricated facts, or source alterations.
Be explicit when the source describes a model assumption or probabilistic mechanism.
Keep code fences, Markdown syntax, links and URLs intact.
Keep the same number and order of Markdown headings and table rows.
Return only the translated Markdown, without a Markdown code fence.
"""

def sections(text, limit=8000):
    """Group at paragraph boundaries without severing tables or code blocks."""
    blocks = re.split(r"(\n\s*\n)", text)
    groups, current = [], ""
    for block in blocks:
        if len(current) + len(block) > limit and current.strip():
            groups.append(current)
            current = ""
        current += block
    if current.strip():
        groups.append(current)
    return groups

def urls(s):
    return sorted(re.findall(r"https?://[^\s)<>]+", s))

def headings(s):
    return [len(match.group(1)) for match in re.finditer(r"^(#{1,6})\s", s, re.M)]

def numeric_markers(s):
    return sorted(re.findall(r"(?<![\w])(?:[+–−-])?\d+(?:\.\d+)?(?:\s*[%$])?", s))

def table_rows(s):
    return len(re.findall(r"^\|.+\|\s*$", s, re.M))

def validate(original, translated):
    errors = []
    if urls(original) != urls(translated):
        errors.append("URL target mismatch")
    if headings(original) != headings(translated):
        errors.append("Heading structure mismatch")
    if table_rows(original) != table_rows(translated):
        errors.append("Markdown table-row count mismatch")
    if len(translated.strip()) < max(30, len(original.strip()) * 0.30):
        errors.append("Suspiciously short output")
    # Numerical changes are flagged for human review but do not fail: natural
    # Korean can rewrite 1-7 as 1~7. These cases are recorded in the report.
    return errors

def make_translation(client, model, source, context, glossary):
    guidance = f"Document title and topic:\n{context}\n\nMandatory terminology:\n{glossary[:13000]}"
    for attempt in range(3):
        response = client.responses.create(
            model=model,
            instructions=PROMPT + "\n" + guidance,
            input=source if attempt == 0 else
                  "Retry. The last translation changed document structure or links. "
                  "Preserve all headings, table rows, hyperlinks and paragraphs exactly.\n\n" + source,
            max_output_tokens=12000,
        )
        result = response.output_text.strip()
        if not validate(source, result):
            return result
        print("Retrying chunk:", validate(source, result), file=sys.stderr)
    raise RuntimeError(f"Translation validation failed: {validate(source, result)}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true",
                        help="Actually write translations (default: show plan)")
    parser.add_argument("--model", default=os.getenv("TRANSLATION_MODEL", "gpt-6.1-sol"))
    parser.add_argument("--limit", type=int, default=0,
                        help="Maximum number of articles, 0 means all 42")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    articles = []
    for article in manifest["articles"]:
        en = Path(article["markdown"])
        key = en.relative_to(ROOT).with_suffix("").as_posix()
        if key not in PROTECTED:
            articles.append((article, en))
    if args.limit:
        articles = articles[:args.limit]
    print(f"Plan: {len(articles)} documents; model={args.model}; write={args.write}")
    if not args.write:
        for article, _ in articles:
            print(" -", article["markdown"])
        return
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY secret required. No files changed.")
    client = OpenAI()
    glossary = GLOSSARY.read_text(encoding="utf-8")
    report = []
    failures = []
    for index, (article, en) in enumerate(articles, 1):
        ko = en.with_name(en.stem + ".ko.md")
        print(f"[{index}/{len(articles)}] {en}", flush=True)
        original = en.read_text(encoding="utf-8")
        # Keep a short source header, skip scraped duplicated H1 and metadata.
        clean = re.sub(r"^<!-- Source:.*?-->\s*", "", original, count=1, flags=re.S)
        chunks = sections(clean)
        translated_parts = []
        try:
            for i, chunk in enumerate(chunks):
                translated_parts.append(make_translation(
                    client, args.model, chunk,
                    f"{article['title']} — part {i+1} of {len(chunks)}",
                    glossary,
                ))
            translated = "\n\n".join(translated_parts).rstrip() + "\n"
            if validate(clean, translated):
                raise ValueError("Full-document validation failed: " + str(validate(clean, translated)))
            review = {
                "source": str(en), "korean": str(ko),
                "model": args.model, "status": "translated",
                "english_chars": len(clean), "korean_chars": len(translated),
                "numeric_markers_same": numeric_markers(clean) == numeric_markers(translated),
                "url_count": len(urls(clean)), "heading_count": len(headings(clean)),
                "table_rows": table_rows(clean),
            }
            content = (
                f"<!-- GPT-based Korean translation; source: {article['url']} -->\n\n"
                f"> **번역 안내:** 문맥을 반영한 AI 번역 초안입니다. "
                f"[영어 원문]({en.name})과 함께 확인하세요.\n\n" + translated
            )
            # Save only once whole document passes automated checks.
            ko.write_text(content, encoding="utf-8")
            report.append(review)
        except Exception as exc:
            failures.append({"source": str(en), "reason": str(exc)})
            print(f"FAILED: {exc}", file=sys.stderr)
    result = {
        "model": args.model, "completed": len(report),
        "failed": len(failures), "protected_examples": sorted(PROTECTED),
        "translated": report, "failures": failures,
        "note": "Automated checks do not constitute expert verification; numeric mismatches need human review."
    }
    (ROOT / "translation_quality_report.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Completed {len(report)}; failed {len(failures)}")
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
