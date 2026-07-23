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


def _kunden_trust_bar():
    items = [
        ("📁", "alle Projekte maßgeschneidert"),
        ("⚡", "Handgeschriebener Code, kein Baukasten"),
        ("⏱️", "Antwort in 24–96 Stunden"),
        ("🔒", "DSGVO-konforme Umsetzung"),
    ]
    chips = [
        div(span(icon, class_="trust-icon"), span(label), class_="trust-item")
        for icon, label in items
    ]
    return div(*chips, class_="trust-bar reveal")


def _ablauf_steps():
    steps = [
        ("01", "Anfrage", "Kurze Nachricht was du vorhast — ich melde mich innerhalb von 24–96 Stunden."),
        ("02", "Konzept & Angebot", "Gemeinsam klären wir Umfang, Design-Richtung und welches Tarifmodell passt."),
        ("03", "Umsetzung", "Handgeschriebener Code, regelmäßige Zwischenstände — keine Blackbox."),
        ("04", "Launch & Support", "Deine Website geht live, Hosting und Anpassungen laufen über dein gewähltes Modell weiter."),
    ]
    cards = [
        div(
            span(num, class_="process-num"),
            h3(title, class_="process-title"),
            p(desc, class_="process-desc"),
            class_="process-step reveal",
            data_delay=str(i * 80),
        )
        for i, (num, title, desc) in enumerate(steps)
    ]
    return div(*cards, class_="process-steps")


def build_kunden_page(css_hash="", js_hash=""):
    cards = [_kunden_project_card(p, i) for i, p in enumerate(KUNDEN_PROJECTS)]
    content = [
        section(
            section_head("01", "Kundenprojekte", KUNDEN_INTRO),
            _kunden_trust_bar(),
            div(*cards, class_="oss-grid"),
            class_="section-block",
        ),
        section(
            section_head("02", "So läuft's ab", "Vier Schritte von der Anfrage bis zur laufenden Website."),
            _ablauf_steps(),
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