#!/usr/bin/env python3
"""Run dependency-free quality checks for the static site.

This file is a check tool only. It is not loaded by the public page.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ElementTree
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_URL = "https://abcderp2.github.io/AI-I-Love-You/"
REQUIRED_FILES = (
    "index.html",
    "style.css",
    "robots.txt",
    "ai.txt",
    "sitemap.xml",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "LICENSE",
    ".nojekyll",
)
FORBIDDEN_SITE_EXTENSIONS = {
    ".js",
    ".mjs",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
}
MAX_HTML_BYTES = 100_000
MAX_CSS_BYTES = 100_000


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.meta: list[dict[str, str]] = []
        self.start_tags: list[tuple[str, dict[str, str]]] = []
        self.links: list[tuple[str, str]] = []
        self.ids: list[str] = []
        self.forbidden_tags: list[str] = []
        self.inline_handlers: list[str] = []
        self.headings: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        normalized_tag = tag.lower()
        normalized_attrs = {
            key.lower(): value or "" for key, value in attrs
        }
        self.start_tags.append((normalized_tag, normalized_attrs))

        if normalized_tag == "html":
            self.html_lang = normalized_attrs.get("lang", "")
        if normalized_tag == "meta":
            self.meta.append(normalized_attrs)
        if normalized_tag == "a":
            self.links.append((normalized_tag, normalized_attrs.get("href", "")))
        if "id" in normalized_attrs:
            self.ids.append(normalized_attrs["id"])
        if normalized_tag in {"script", "iframe", "frame", "object", "embed", "form"}:
            self.forbidden_tags.append(normalized_tag)
        for key in normalized_attrs:
            if key.startswith("on"):
                self.inline_handlers.append(key)
        if normalized_tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(normalized_tag)


def read_text(relative_path: str, errors: list[str]) -> str:
    path = ROOT / relative_path
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        errors.append(f"missing file: {relative_path}")
    except UnicodeDecodeError:
        errors.append(f"not UTF-8: {relative_path}")
    return ""


def check_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")


def check_html(errors: list[str]) -> None:
    html = read_text("index.html", errors)
    if not html:
        return

    if not html.lstrip().lower().startswith("<!doctype html>"):
        errors.append("index.html must begin with an HTML5 doctype")

    parser = SiteParser()
    try:
        parser.feed(html)
    except Exception as exc:
        errors.append(f"index.html could not be parsed: {exc}")
        return

    if parser.html_lang != "ja":
        errors.append("index.html must declare html lang=ja")

    meta_by_name = {
        item.get("name", "").lower(): item.get("content", "")
        for item in parser.meta
        if item.get("name")
    }
    charset_ok = any(
        item.get("charset", "").lower().replace("-", "") == "utf8"
        for item in parser.meta
    )
    if not charset_ok:
        errors.append("index.html must declare UTF-8")

    viewport = meta_by_name.get("viewport", "")
    if "width=device-width" not in viewport or "initial-scale=1" not in viewport:
        errors.append("viewport must include width=device-width and initial-scale=1")

    title_match = re.search(r"<title>\s*(.*?)\s*</title>", html, re.IGNORECASE | re.DOTALL)
    if not title_match or not title_match.group(1).strip():
        errors.append("index.html must contain a non-empty title")

    if not meta_by_name.get("description", "").strip():
        errors.append("index.html must contain a meta description")

    canonical_links = [
        attrs.get("href", "")
        for tag, attrs in parser.start_tags
        if tag == "link" and "canonical" in attrs.get("rel", "").lower().split()
    ]
    if canonical_links != [CANONICAL_URL]:
        errors.append("index.html must contain exactly one canonical URL")

    if meta_by_name.get("referrer") != "no-referrer":
        errors.append("index.html must set referrer to no-referrer")

    csp_values = [
        attrs.get("content", "")
        for attrs in parser.meta
        if attrs.get("http-equiv", "").lower() == "content-security-policy"
    ]
    if len(csp_values) != 1:
        errors.append("index.html must contain exactly one Content-Security-Policy meta element")
    else:
        csp = csp_values[0]
        required_directives = (
            "default-src 'self'",
            "base-uri 'none'",
            "connect-src 'none'",
            "form-action 'none'",
            "img-src 'none'",
            "object-src 'none'",
            "script-src 'none'",
            "style-src 'self'",
        )
        for directive in required_directives:
            if directive not in csp:
                errors.append(f"CSP is missing: {directive}")

    if len(parser.ids) != len(set(parser.ids)):
        errors.append("index.html contains duplicate id values")

    if parser.headings.count("h1") != 1:
        errors.append("index.html must contain exactly one h1")
    if "h2" not in parser.headings:
        errors.append("index.html must contain at least one h2")
    if not any(
        attrs.get("lang", "").lower().split("-")[0] == "en"
        for tag, attrs in parser.start_tags
    ):
        errors.append("index.html must mark English content with lang=en")

    if parser.forbidden_tags:
        errors.append(
            "index.html contains forbidden executable or stateful tags: "
            + ", ".join(sorted(set(parser.forbidden_tags)))
        )
    if parser.inline_handlers:
        errors.append(
            "index.html contains inline event handlers: "
            + ", ".join(sorted(set(parser.inline_handlers)))
        )
    if re.search(r"javascript\s*:", html, re.IGNORECASE):
        errors.append("index.html must not contain javascript URLs")
    if "data:" in html.lower():
        errors.append("index.html must not contain data URLs")

    stylesheet_links = [
        attrs.get("href", "")
        for tag, attrs in parser.start_tags
        if tag == "link" and "stylesheet" in attrs.get("rel", "").lower().split()
    ]
    if stylesheet_links != ["style.css"]:
        errors.append("index.html must load exactly the local style.css")

    for tag, attrs in parser.start_tags:
        if tag not in {"link", "script", "img", "iframe", "frame", "object", "embed", "audio", "video", "source"}:
            continue
        reference = attrs.get("href") or attrs.get("src") or attrs.get("data")
        if not reference:
            continue
        parsed = urlsplit(reference)
        if parsed.scheme in {"http", "https"} or reference.startswith("//"):
            is_canonical = tag == "link" and "canonical" in attrs.get("rel", "").lower().split()
            if not is_canonical:
                errors.append(f"external runtime resource is not allowed: {reference}")

    for tag, href in parser.links:
        if not href:
            errors.append("an anchor is missing href")
            continue
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc:
            if parsed.scheme != "https" or parsed.netloc.lower() != "github.com":
                errors.append(f"external anchor is not allowlisted: {href}")
            continue
        if href.startswith("#"):
            target = href[1:].split("?", 1)[0]
            if target and target not in parser.ids:
                errors.append(f"anchor target does not exist: {href}")
            continue

        relative_path = parsed.path or "index.html"
        if relative_path.endswith("/"):
            relative_path += "index.html"
        target_path = (ROOT / relative_path.lstrip("/")).resolve()
        try:
            target_path.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"anchor leaves the repository: {href}")
            continue
        if not target_path.is_file():
            errors.append(f"local anchor target does not exist: {href}")


def check_css(errors: list[str]) -> None:
    css = read_text("style.css", errors)
    if not css:
        return
    if "@import" in css.lower():
        errors.append("style.css must not import external or generated styles")
    if re.search(r"url\s*\(", css, re.IGNORECASE):
        errors.append("style.css must not load resources with url()")
    if "http://" in css.lower() or "https://" in css.lower():
        errors.append("style.css must not contain external URLs")
    if "data:" in css.lower():
        errors.append("style.css must not contain data URLs")


def check_local_files(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        if path.suffix.lower() in FORBIDDEN_SITE_EXTENSIONS:
            errors.append(f"forbidden site asset or script: {path.relative_to(ROOT)}")

    index_size = (ROOT / "index.html").stat().st_size if (ROOT / "index.html").exists() else 0
    css_size = (ROOT / "style.css").stat().st_size if (ROOT / "style.css").exists() else 0
    if index_size > MAX_HTML_BYTES:
        errors.append("index.html exceeds the 100 KB source budget")
    if css_size > MAX_CSS_BYTES:
        errors.append("style.css exceeds the 100 KB source budget")


def check_text_policies(errors: list[str]) -> None:
    robots = read_text("robots.txt", errors)
    if "User-agent: *" not in robots or "Allow: /" not in robots:
        errors.append("robots.txt must allow well-behaved crawlers explicitly")
    if f"Sitemap: {CANONICAL_URL}sitemap.xml" not in robots:
        errors.append("robots.txt must point to the canonical sitemap")

    ai = read_text("ai.txt", errors)
    if f"Canonical URL: {CANONICAL_URL}" not in ai:
        errors.append("ai.txt must declare the canonical URL")
    if "does not claim" not in ai.lower() and "主張しません" not in ai:
        errors.append("ai.txt must state that it is not a universal crawler protocol")

    sitemap = read_text("sitemap.xml", errors)
    try:
        root = ElementTree.fromstring(sitemap)
        locations = [
            element.text.strip()
            for element in root.iter()
            if element.tag.lower().endswith("loc") and element.text
        ]
        if locations != [CANONICAL_URL]:
            errors.append("sitemap.xml must contain exactly the canonical URL")
        lastmods = [
            element.text.strip()
            for element in root.iter()
            if element.tag.lower().endswith("lastmod") and element.text
        ]
        for lastmod in lastmods:
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", lastmod):
                errors.append(f"sitemap.xml has an invalid lastmod: {lastmod}")
    except ElementTree.ParseError as exc:
        errors.append(f"sitemap.xml is not valid XML: {exc}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_html(errors)
    check_css(errors)
    check_local_files(errors)
    check_text_policies(errors)

    if errors:
        print("FAIL: static site quality checks")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: static site quality checks")
    print("No external runtime resources, scripts, forms, duplicate anchors, or broken local anchors were found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
