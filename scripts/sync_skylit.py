#!/usr/bin/env python3
"""Archive Skylit /learn pages to HTML and Markdown. Run only with permission."""
import json, re, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

BASE = "https://www.skylit.ai"
ROOT = BASE + "/learn"
OUT = Path("docs/skylit")
CATEGORIES = {
    "skylit academy": "academy",
    "the greeks": "greeks",
    "heatseeker: gamma & vanna": "heatseeker",
    "flowseeker": "flowseeker",
    "tools & comparisons": "tools",
}

def get(session, url):
    r = session.get(url, timeout=45)
    r.raise_for_status()
    if "html" not in r.headers.get("content-type", ""):
        raise ValueError("Not an HTML response")
    return r.text

def valid_link(href):
    url = urljoin(BASE, href)
    p = urlparse(url)
    path = p.path.rstrip("/")
    if p.netloc not in ("www.skylit.ai", "skylit.ai"):
        return None
    if not re.fullmatch(r"/learn/[^/]+", path):
        return None
    return BASE + path

def discover(html):
    soup = BeautifulSoup(html, "html.parser")
    seen = {}
    for heading in soup.find_all("h2"):
        cat = CATEGORIES.get(heading.get_text(" ", strip=True).lower())
        if not cat:
            continue
        section = heading.find_parent("section")
        links = []
        if section:
            links = section.select("a[href]")
        else:
            for el in heading.next_elements:
                if getattr(el, "name", "") == "h2":
                    break
                if getattr(el, "name", "") == "a" and el.get("href"):
                    links.append(el)
        for a in links:
            url = valid_link(a.get("href", ""))
            if url:
                seen[url] = cat
    for a in soup.select("a[href]"):
        url = valid_link(a["href"])
        if url and url not in seen:
            seen[url] = "other"
    return seen

def extract(html):
    soup = BeautifulSoup(html, "html.parser")
    h1 = soup.find("h1")
    if not h1:
        raise ValueError("No article heading found")
    title = h1.get_text(" ", strip=True)
    candidates = [el for el in soup.select("article, main, .prose, [itemprop=articleBody]") if el.find("h1")]
    body = candidates[-1] if candidates else h1.parent
    if not candidates:
        while body.parent and len(body.get_text(" ", strip=True)) < 1200:
            body = body.parent
    clean = BeautifulSoup(str(body), "html.parser")
    for el in clean.select("script, style, nav, footer, header, aside, button, form, noscript"):
        el.decompose()
    for a in clean.select("a[href]"):
        a["href"] = urljoin(BASE, a["href"])
    for img in clean.select("img[src]"):
        img["src"] = urljoin(BASE, img["src"])
    md = markdownify(str(clean), heading_style="ATX").strip()
    if len(md) < 300:
        raise ValueError("Extracted article too short; inspect page structure")
    return title, md

def main():
    session = requests.Session()
    session.headers["User-Agent"] = "PersonalSkylitArchive/1.0 (authorized)"
    OUT.mkdir(parents=True, exist_ok=True)
    hub = get(session, ROOT)
    (OUT / "_landing.html").write_text(hub, encoding="utf-8")
    found = discover(hub)
    if not found:
        raise RuntimeError("No articles discovered; page structure may have changed")
    results, failures = [], []
    for idx, (url, category) in enumerate(found.items(), 1):
        slug = urlparse(url).path.rstrip("/").split("/")[-1]
        folder = OUT / category
        folder.mkdir(exist_ok=True)
        print(f"[{idx}/{len(found)}] {url}", flush=True)
        try:
            html = get(session, url)
            title, md = extract(html)
            html_path = folder / (slug + ".html")
            md_path = folder / (slug + ".md")
            html_path.write_text(html, encoding="utf-8")
            md_path.write_text(f"<!-- Source: {url} -->\n\n# {title}\n\n{md}\n", encoding="utf-8")
            results.append({"title": title, "url": url, "category": category,
                            "html": str(html_path), "markdown": str(md_path)})
        except Exception as exc:
            print("FAILED", url, exc, flush=True)
            failures.append({"url": url, "error": str(exc)})
        time.sleep(1)
    manifest = {"source": ROOT, "checked_at": datetime.now(timezone.utc).isoformat(),
                "discovered": len(found), "saved": len(results),
                "articles": results, "failures": failures}
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Skylit Learn Archive", "", f"Source: {ROOT}", "",
             f"Saved **{len(results)} / {len(found)}** articles.", ""]
    for category in dict.fromkeys(a["category"] for a in results):
        lines += [f"## {category.title()}", ""]
        for a in (item for item in results if item["category"] == category):
            p = Path(a["markdown"]).relative_to(OUT).as_posix()
            lines.append(f'- [{a["title"]}]({p}) · [Original]({a["url"]})')
        lines.append("")
    (OUT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    if failures:
        raise SystemExit(f"{len(failures)} document(s) failed; see docs/skylit/manifest.json")
    print(f"Saved {len(results)} articles.")

if __name__ == "__main__":
    main()
