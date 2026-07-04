"""
components/oss.py
"""

from htmforge.elements import div, span, a, h3, p, section

from data import SITE_URL, OSS_PROJECTS
from .shared import tag_chip, section_head, _page_shell


def _oss_project_card(proj: dict, index: int):
    meta_rows = [
        div(span(k, class_="meta-key"), span(v, class_="meta-val"), class_="meta-row")
        for k, v in proj["meta"]
    ]
    link_btns = [
        a(
            lnk["label"], href=lnk["url"], target="_blank", rel="noopener",
            class_=f"svc-btn {'svc-btn-secondary' if not lnk['primary'] else ''}",
        )
        for lnk in proj["links"]
    ]
    return div(
        div(
            span(proj["emoji"], class_="oss-icon"),
            div(tag_chip(proj["tag"]), span(proj["tagline"], class_="svc-tagline"), class_="svc-badges"),
            class_="svc-top",
        ),
        h3(proj["label"], class_="svc-name"),
        p(proj["desc"], class_="svc-desc"),
        div(*meta_rows, class_="oss-meta"),
        div(*link_btns, class_="svc-actions"),
        class_="oss-card reveal",
        data_delay=str(index * 100),
    )


def build_opensource_page(css_hash="", js_hash=""):
    cards = [_oss_project_card(p, i) for i, p in enumerate(OSS_PROJECTS)]
    content = [
        section(
            section_head(
                "01", "Open Source",
                "Bibliotheken die aus echten Projekten entstehen — auf PyPI veröffentlicht, "
                "MIT-lizenziert, produktionsreif. Kein Spielzeug.",
            ),
            div(*cards, class_="oss-grid"),
            class_="section-block",
        ),
    ]
    return _page_shell(
        "Open Source", "Python-Bibliotheken von NepiDesk — MIT-lizenziert, auf PyPI.",
        "opensource", content, css_hash, js_hash,
        canonical=SITE_URL + "/opensource",
    )