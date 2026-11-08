#!/usr/bin/env python3
"""Translate archived Skylit Markdown into Korean using an offline Argos model.

Preserves source English, Markdown link destinations, fenced code and HTML structure.
Generated Korean translations are machine drafts, not professionally reviewed.
"""
import json
import re
from pathlib import Path

import argostranslate.package
import argostranslate.translate
import markdown
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as to_md

ROOT = Path("docs/skylit")
MANIFEST = ROOT / "manifest.json"
SKIP_TAGS = {"pre", "code", "script", "style", "svg", "math"}
GLOSSARY = {
    "Gamma Exposure": "감마 익스포저(GEX)",
    "Vanna Exposure": "바나 익스포저(VEX)",
    "dealer positioning": "딜러 포지셔닝",
    "market maker": "마켓 메이커",
    "open interest": "미결제약정",
    "implied volatility": "내재변동성",
    "support": "지지",
    "resistance": "저항",
}
def setup_translation():
    installed = argostranslate.translate.get_installed_languages()
    en = next((x for x in installed if x.code == "en"), None)
    ko = next((x for x in installed if x.code == "ko"), None)
    if not en or not ko:
        argostranslate.package.update_package_index()
        pkgs = argostranslate.package.get_available_packages()
        pkg = next((p for p in pkgs if p.from_code == "en" and p.to_code == "ko"), None)
        if pkg is None:
            raise RuntimeError("Argos English→Korean language package not available")
        argostranslate.package.install_from_path(pkg.download())
        installed = argostranslate.translate.get_installed_languages()
        en = next(x for x in installed if x.code == "en")
        ko = next(x for x in installed if x.code == "ko")
    return en.get_translation(ko)

def translate_text(text, translator, cache):
    if not text.strip() or not re.search("[A-Za-z]", text):
        return text
    if text.strip() in cache:
        out = cache[text.strip()]
    else:
        out = translator.translate(text.strip())
        cache[text.strip()] = out
    # Keep original surrounding spaces, important around inline links and emphasis.
    leading = text[:len(text)-len(text.lstrip())]
    trailing = text[len(text.rstrip()):]
    return leading + out + trailing

def translate_document(source, translator, cache):
    # Ignore provenance comment; reinsert it after translation.
    source = re.sub(r"^<!-- Source:.*?-->\s*", "", source, count=1, flags=re.S)
    html = markdown.markdown(source, extensions=["extra", "tables", "fenced_code", "sane_lists"])
    soup = BeautifulSoup(html, "html.parser")
    for node in list(soup.find_all(string=True)):
        if not isinstance(node, NavigableString):
            continue
        if node.parent and node.parent.name in SKIP_TAGS:
            continue
        original = str(node)
        if original.strip():
            node.replace_with(translate_text(original, translator, cache))
    return to_md(str(soup), heading_style="ATX", bullets="-").strip()

def main():
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    tr = setup_translation()
    cache_file = ROOT / ".translation_cache.json"
    cache = json.loads(cache_file.read_text(encoding="utf-8")) if cache_file.exists() else {}
    output = []
    for i, article in enumerate(data["articles"], 1):
        en = Path(article["markdown"])
        ko = en.with_name(en.stem + ".ko.md")
        if ko.exists():
            print(f"SKIP existing translation: {ko}", flush=True)
            article["korean"] = str(ko)
            output.append(article)
            continue
        translated = translate_document(en.read_text(encoding="utf-8"), tr, cache)
        ko.write_text(
            f"<!-- Machine translation; review against original. Source: {article['url']} -->\n\n"
            + f"> **번역 안내:** 이 문서는 자동 번역 초안입니다. 수치·수식·거래 판단은 [영어 원문]({en.name})을 확인하세요.\n\n"
            + translated + "\n", encoding="utf-8")
        article["korean"] = str(ko)
        output.append(article)
        print(f"[{i}/{len(data['articles'])}] {ko}", flush=True)
        if i % 5 == 0:
            cache_file.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    cache_file.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    data["translation_method"] = "Argos Translate en→ko, automatic draft"
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Skylit Learn · 한국어 번역 목차", "", "> 자동 번역 초안이며 문맥·전문용어 검수가 필요합니다.", ""]
    for category in dict.fromkeys(a["category"] for a in output):
        lines += [f"## {category.title()}", ""]
        for a in output:
            if a["category"] == category:
                en = Path(a["markdown"]).relative_to(ROOT).as_posix()
                ko = Path(a["korean"]).relative_to(ROOT).as_posix()
                lines.append(f"- [{a['title']}]({ko}) · [English]({en})")
        lines.append("")
    (ROOT / "KO_INDEX.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
