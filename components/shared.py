"""
components/shared.py
Gemeinsame Bausteine: Atoms (tag_chip, section_head) und die Seiten-Shell
(_head, _page_shell), die von allen Unterseiten genutzt wird.
"""

from htmforge import render
from htmforge.elements import div, span, p, h2, head, body, html, title, link, meta, script, main

from data import SITE_URL
from .header import build_header
from .footer import build_footer


def tag_chip(tag: str):
    labels = {"oss": "OSS", "dev": "DEV", "sys": "SYS", "kunde": "KUNDE"}
    return span(labels.get(tag, tag), class_=f"tag tag-{tag}")


def section_head(num: str, title: str, subtitle: str = ""):
    return div(
        div(span(num, class_="section-num"), span("·", class_="section-dot"), class_="section-meta"),
        h2(
            span("", class_="typewriter-text"),
            span("▌", class_="typewriter-cursor"),
            data_typewriter=title,
            class_="section-title typewriter",
        ),
        p(subtitle, class_="section-sub") if subtitle else span(""),
        class_="section-head",
    )


def _head(page_title: str, description: str, css_hash: str = "", canonical: str = SITE_URL):
    json_ld = """{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Moritz Mond",
  "url": "https://nepidesk.de",
  "jobTitle": "Freelance Developer",
  "description": "Freelance-Entwickler für individuelle Kunden-Websites, Python Web Development und self-hosted Open-Source-Tools.",
  "sameAs": [
    "https://github.com/mondi04",
    "https://pypi.org/user/mondi04/"
  ]
}"""
    return head(
        meta(charset="UTF-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        meta(name="description", content=description),
        meta(name="author",      content="Moritz · NepiDesk"),
        meta(name="robots",      content="index, follow"),
        meta(property="og:title",       content=page_title),
        meta(property="og:description", content=description),
        meta(property="og:type",        content="website"),
        meta(property="og:url",         content=canonical),
        meta(property="og:site_name",   content="NepiDesk"),
        meta(property="og:locale",      content="de_DE"),
        meta(property="og:image",       content=SITE_URL + "/static/og-image.png"),
        meta(property="og:image:width",  content="1200"),
        meta(property="og:image:height", content="630"),
        meta(property="og:image:alt",    content="NepiDesk - Websites für Kunden · Python · Open Source"),
        meta(name="twitter:image",       content=SITE_URL + "/static/og-image.png"),
        meta(name="twitter:card",        content="summary_large_image"),
        meta(name="twitter:title",       content=page_title),
        meta(name="twitter:description", content=description),
        title(page_title),
        link(rel="canonical", href=canonical),
        link(rel="preload", href="/static/css/fonts.css", as_="style"),
        link(rel="preload", href=f"/static/css/main.css?v={css_hash}", as_="style"),
        link(rel="stylesheet", href="/static/css/fonts.css"),
        link(rel="stylesheet", href=f"/static/css/main.css?v={css_hash}"),
        link(rel="icon", type="image/x-icon", href="/static/favicon.ico"),
        link(rel="apple-touch-icon", sizes="180x180", href="/static/apple-touch-icon.png"),
        script(src=f"/static/js/htmx.min.js?v={css_hash}", defer=True),
        script(type="application/ld+json", _content=json_ld),
    )


def _page_shell(page_title: str, description: str, active: str, content, css_hash="", js_hash="", canonical: str = SITE_URL):
    """Generische Seiten-Shell für alle Unterseiten."""
    page = html(
        _head(page_title + " — NepiDesk", description, css_hash, canonical),
        body(
            build_header(active),
            main(*content, class_="page-main"),
            build_footer(),
            div(id="toast-slot", class_="toast-slot"),
            script(src=f"/static/js/main.js?v={js_hash}", defer=True),
        ),
        lang="de",
    )
    return "<!DOCTYPE html>\n" + render(page)