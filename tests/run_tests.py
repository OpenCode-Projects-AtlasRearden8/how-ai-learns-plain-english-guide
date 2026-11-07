#!/usr/bin/env python3
"""Self-tests for the How AI Learns plain-English guide.

Verifies, with zero dependencies:
  1. the expected project structure exists,
  2. the LICENSE copyright line is exact and README credits the LLC,
  3. every internal markdown/HTML link inside docs/ and site/ resolves,
  4. all site HTML parses with balanced structure,
  5. the glossary is complete (every entry has a definition, anchors match),
  6. no file looks like it contains a secret (keys, tokens),
  7. the docs keep their house-distinctions (not a dictionary, not a
     benchmark scorecard).

Run:  python3 tests/run_tests.py
"""

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "STATUS.md",
    "docs/00-start-here.md",
    "docs/01-the-journey-before-the-answer.md",
    "docs/02-training-on-text.md",
    "docs/03-next-word-prediction.md",
    "docs/04-tuning-and-feedback.md",
    "docs/05-why-models-invent-things.md",
    "docs/06-model-name-decoder.md",
    "docs/07-update-cadence.md",
    "docs/08-cheat-sheet.md",
    "docs/glossary.md",
    "site/index.html",
    "site/journey.html",
    "site/names.html",
    "site/glossary.html",
    "site/styles.css",
    "site/app.js",
]

CHAPTER_MIN_WORDS = {
    "00-start-here.md": 500,
    "01-the-journey-before-the-answer.md": 550,
    "02-training-on-text.md": 550,
    "03-next-word-prediction.md": 550,
    "04-tuning-and-feedback.md": 550,
    "05-why-models-invent-things.md": 550,
    "06-model-name-decoder.md": 550,
    "07-update-cadence.md": 450,
    "08-cheat-sheet.md": 280,
    "glossary.md": 400,
}

COPYRIGHT_LINE = "Copyright (c) 2026 Asdale Dynamics, LLC"
REQUIRED_SITE_PAGES = {
    "index.html": ["How AI Learns", "next word at a time", "two clocks"],
    "journey.html": ["Guess the Next Word", "cafe", "temperature"],
    "names.html": ["Model Name Decoder", "four-part", "cadence"],
    "glossary.html": ["Plain-English Glossary", "temperature",
                      "hallucination"],
}
REQUIRED_HOOKS = ["glossary-search", "nextword-form", "temp-slider",
                  "decoder-form", "flip-btn"]

failures = []
passes = []


def check(name, condition, detail=""):
    if condition:
        passes.append(name)
    else:
        failures.append(f"{name}{' — ' + detail if detail else ''}")


def md_link_targets(text):
    """Yield relative link targets from markdown link syntax."""
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
        yield m.group(1)


def strip_anchors(target):
    return target.split("#", 1)[0]


def test_files_exist():
    for rel in REQUIRED_FILES:
        check(f"file exists: {rel}", (ROOT / rel).is_file())


def test_license_exact():
    text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    check("LICENSE is MIT", "MIT License" in text)
    lines = text.splitlines()
    copyright_lines = [ln for ln in lines if ln.startswith("Copyright")]
    check("LICENSE copyright line is exact",
          copyright_lines and copyright_lines[0] == COPYRIGHT_LINE,
          detail=copyright_lines[0] if copyright_lines else "none found")


def test_readme_credits():
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    check("README credits Asdale Dynamics, LLC", "Asdale Dynamics, LLC" in text)


def test_no_secrets():
    secret_re = re.compile(
        r"(sk-[A-Za-z0-9]{16,}|ghp_[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}"
        r"|(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,})",
        re.IGNORECASE)
    offenders = []
    for path in ROOT.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            try:
                content = path.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if secret_re.search(content):
                offenders.append(str(path.relative_to(ROOT)))
    check("no secrets detected", not offenders, detail=", ".join(offenders))


def test_docs_links_and_content():
    for md in sorted(DOCS.glob("*.md")):
        text = md.read_text(encoding="utf-8")
        check(f"{md.name} has an H1 title", text.lstrip().startswith("# "))
        words = len(re.findall(r"\S+", text))
        floor = CHAPTER_MIN_WORDS.get(md.name, 400)
        check(f"{md.name} is substantive ({words} words)", words >= floor)
        for target in md_link_targets(text):
            if target.startswith(("http://", "https://")) or target.startswith("mailto:"):
                continue
            resolved = (md.parent / strip_anchors(target)).resolve()
            check(f"{md.name} link resolves: {target}", resolved.is_file())
    # every main chapter is wired into the start-here page
    start = (DOCS / "00-start-here.md").read_text(encoding="utf-8")
    for chapter in ["01-the-journey-before-the-answer.md",
                    "02-training-on-text.md", "03-next-word-prediction.md",
                    "04-tuning-and-feedback.md", "05-why-models-invent-things.md",
                    "06-model-name-decoder.md", "07-update-cadence.md"]:
        check(f"00-start-here links {chapter}", chapter in start)


def test_house_distinctions():
    """This guide must keep its lane vs. the two sibling projects."""
    start = (DOCS / "00-start-here.md").read_text(encoding="utf-8")
    check("distinguishes itself from ai-glossary-pocketbook",
          "ai-glossary-pocketbook" in start)
    check("distinguishes itself from ai-benchmarks-explained-guide",
          "ai-benchmarks-explained-guide" in start)
    names = (DOCS / "06-model-name-decoder.md").read_text(encoding="utf-8")
    check("decoder uses the fictional teaching families",
          "Checkers" in names and "Widget" in names)
    cadence = (DOCS / "07-update-cadence.md").read_text(encoding="utf-8")
    check("cadence chapter covers quiet re-seasoning",
          "seasoning" in cadence.lower())


def test_glossary_covers_html_anchors():
    """Every glossary anchor linked from anywhere must have a real target."""
    link_anchors = set()
    for base in (DOCS, SITE):
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix not in {".md", ".html"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for m in re.finditer(r"\((glossary\.md#([\w-]+))\)", text):
                link_anchors.add(m.group(2))
    gloss_md = (DOCS / "glossary.md").read_text(encoding="utf-8")
    dt_lines = [ln.strip().lstrip("- ") for ln in gloss_md.splitlines()
                if ln.startswith("- **")]
    check("glossary.md has 15+ entries", len(dt_lines) >= 15)
    gloss_html = (SITE / "glossary.html").read_text(encoding="utf-8")
    html_anchors = set(re.findall(r'<div id="([\w-]+)"', gloss_html))
    entries = re.findall(r'<div id="([\w-]+)">\s*<dt>(.*?)</dt>\s*<dd>(.*?)</dd>',
                         gloss_html, flags=re.DOTALL)
    for anchor, term, definition in entries:
        check(f"glossary entry '{anchor}' defined",
              bool(term.strip()) and len(definition.strip()) > 30)
    check("glossary.html has 15+ entries", len(entries) >= 15)
    for anchor in link_anchors:
        check(f"glossary anchor target exists: {anchor}", anchor in html_anchors)


class StructureParser(HTMLParser):
    """Crude structural check: track open/close pairing of container tags."""

    VOID = {"meta", "link", "br", "img", "input", "hr", "source", "wbr"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag in self.VOID:
            return
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID:
            return
        if not self.stack:
            self.errors.append(f"</{tag}> with empty stack")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"</{tag}> but open is <{self.stack[-1]}>")


def test_site_html_structure_and_targets():
    for name in REQUIRED_SITE_PAGES:
        page = SITE / name
        text = page.read_text(encoding="utf-8")
        parser = StructureParser()
        parser.feed(text)
        check(f"{name} parses with balanced structure",
              not parser.errors and not parser.stack,
              detail="; ".join(parser.errors) or f"unclosed {parser.stack[:3]}")
        for must in REQUIRED_SITE_PAGES[name]:
            check(f"{name} contains '{must}'", must in text)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:", "#")) or url == "":
                continue
            resolved = (SITE / strip_anchors(url)).resolve()
            check(f"{name} asset/link resolves: {url}", resolved.is_file())
        external_assets = [u for u in re.findall(r'(?:href|src)="([^"]+)"', text)
                           if u.startswith(("http://", "https://"))]
        check(f"{name} has no external asset links", not external_assets,
              detail=", ".join(external_assets))
        check(f"{name} has no tracking", not re.search(
            r"https?://[^\"]*("
            r"analytics|pixel|gtag|matomo|fathom|plausible\.io|"
            r"google-analytics|doubleclick|hotjar)",
            text, re.IGNORECASE))


def test_site_scripts_and_hooks():
    for name in ("styles.css", "app.js"):
        body = (SITE / name).read_text(encoding="utf-8")
        check(f"{name} is non-trivial", len(body) >= 1000)
    js = (SITE / "app.js").read_text(encoding="utf-8")
    all_site = "".join((SITE / n).read_text(encoding="utf-8")
                       for n in REQUIRED_SITE_PAGES)
    for hook in REQUIRED_HOOKS:
        check(f"interactivity wired: {hook}", hook in js and hook in all_site)
    # system fonts only: no external font imports
    css = (SITE / "styles.css").read_text(encoding="utf-8")
    check("styles.css imports no external fonts", "@import" not in css
          and "fonts.googleapis" not in css and "@font-face" not in css)


def test_no_pending_garbage():
    """Guard-rail: reject obvious draft artifacts left in prose."""
    bad_patterns = [
        r"[\u4e00-\u9fff\u3040-\u30ff]",  # stray CJK/kana
        r"\bTODO\b|\bFIXME\b|\bXXX\b",
        r"Co-authored-by",
    ]
    offenders = []
    for base in (DOCS, SITE):
        for path in sorted(base.rglob("*")):
            if not path.is_file() or path.suffix not in {".md", ".html", ".js", ".css"}:
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            for pat in bad_patterns:
                if re.search(pat, text):
                    offenders.append(f"{path.relative_to(ROOT)}: {pat}")
    check("no draft artifacts", not offenders, detail="; ".join(offenders))


def main():
    test_files_exist()
    test_license_exact()
    test_readme_credits()
    test_no_secrets()
    test_docs_links_and_content()
    test_house_distinctions()
    test_glossary_covers_html_anchors()
    test_site_html_structure_and_targets()
    test_site_scripts_and_hooks()
    test_no_pending_garbage()

    print(f"PASS {len(passes)} checks")
    for p in passes:
        print(f"  ok: {p}")
    if failures:
        print(f"\nFAIL {len(failures)} checks")
        for f in failures:
            print(f"  FAIL: {f}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
