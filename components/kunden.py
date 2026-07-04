"""
components/kunden.py
Kundenprojekte — das Hauptgeschäft von NepiDesk: individuelle Websites für
Vereine, Selbstständige und kleine Unternehmen.
"""

from htmforge.elements import div, span, h2, h3, p, a, section

from data import SITE_URL, KUNDEN_INTRO, KUNDEN_PROJECTS
from .shared import tag_chip, section_head, _page_shell


def _kunden_project_card(proj: dict, index: int):
    meta_rows = [
        div(span(k, class_="meta-key"), span(v, class_="meta-val"), class_="meta-row")
        for k, v in proj["meta"]
    ]
    return div(
        div(
            span(proj["emoji"], class_="oss-icon"),
            div(
                tag_chip("kunde"),
                span(proj["tagline"], class_="svc-tagline"),
                class_="svc-badges",
            ),
            class_="svc-top",
        ),
        h3(proj["label"], class_="svc-name"),
        p(proj["desc"], class_="svc-desc"),
        div(*meta_rows, class_="oss-meta"),
        a("Website ansehen ↗", href=proj["url"], target="_blank", rel="noopener", class_="svc-btn")
        if proj.get("url") else span(""),
        class_="oss-card reveal",
        data_delay=str(index * 100),
    )


def build_kunden_page(css_hash="", js_hash=""):
    cards = [_kunden_project_card(p, i) for i, p in enumerate(KUNDEN_PROJECTS)]
    content = [
        section(
            section_head("01", "Kundenprojekte", KUNDEN_INTRO),
            div(*cards, class_="oss-grid"),
            class_="section-block",
        ),
        section(
            div(
                h2("Eigene Website geplant?", class_="cta-banner-title"),
                p(
                    "Ob Verein, Selbstständigkeit oder kleines Unternehmen — ich baue "
                    "dir eine schnelle, individuelle Website ohne Baukasten-Look. "
                    "Schreib mir kurz was du vorhast.",
                    class_="cta-banner-sub",
                ),
                a("Projekt anfragen", href="/kontakt?betreff=website", class_="cta-primary"),
                class_="cta-banner reveal",
            ),
            class_="section-block",
        ),
    ]
    return _page_shell(
        "Kundenprojekte",
        "Individuelle Websites für Kunden — Vereine, Selbstständige, kleine Unternehmen.",
        "kunden", content, css_hash, js_hash,
        canonical=SITE_URL + "/kunden",
    )