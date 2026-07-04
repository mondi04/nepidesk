"""
components/home.py
Startseite: Hero, Ticker, Preview-Grid, Stack-Section.
Kundenprojekte stehen bewusst zuerst im Preview-Grid — Hauptgeschäft.
"""

from htmforge import render
from htmforge.elements import div, span, a, p, h3, section, html, body, main, script

from data import (
    HERO_CLAIM, HERO_SUB, TICKER_ITEMS, STACK,
    HOME_KUNDEN_PREVIEW, HOME_OSS_PREVIEW, HOME_SOFTWARE_PREVIEW,
    HOME_INFRA_PREVIEW, HOME_TARIFE_PREVIEW,
)
from .shared import tag_chip, section_head, _head
from .header import build_header
from .footer import build_footer


def build_hero():
    return section(
        div(class_="parallax-grid", data_speed="0.3"),
        div(class_="parallax-glow parallax-glow-1", data_speed="0.5"),
        div(class_="parallax-glow parallax-glow-2", data_speed="0.2"),
        div(
            div(
                span("", class_="eyebrow-dot"),
                span("Websites für Kunden · Freelance · Remote", class_="eyebrow-text"),
                class_="eyebrow",
            ),
            div(
                span("NEPI", class_="hero-word hero-word-1"),
                span("DESK", class_="hero-word hero-word-2"),
                class_="hero-logotype",
            ),
            p(HERO_CLAIM, class_="hero-claim"),
            p(HERO_SUB, class_="hero-sub"),
            div(
                a("Kundenprojekte ansehen", href="/kunden", class_="cta-primary"),
                a("Tarife ansehen", href="/tarife", class_="cta-secondary"),
                a("Kontakt", href="/kontakt", class_="cta-secondary"),
                class_="hero-ctas",
            ),
            div(class_="hud-corner hud-tl"),
            div(class_="hud-corner hud-tr"),
            div(class_="hud-corner hud-bl"),
            div(class_="hud-corner hud-br"),
            class_="hero-box",
        ),
        class_="hero-section", id="hero",
    )


def build_ticker():
    def make_items():
        return [
            div(
                span(t["key"],    class_="spec-key"),
                span(t["value"],  class_="spec-val"),
                span(t["detail"], class_="spec-detail"),
                class_="spec-item",
            )
            for t in TICKER_ITEMS
        ]
    all_items = make_items() * 4
    return div(div(*all_items, class_="ticker-track"), class_="specs-ticker")


def build_preview_card(data: dict, index: int):
    return div(
        div(
            span(data["emoji"], class_="preview-icon"),
            tag_chip(data["tag"]),
            class_="preview-top",
        ),
        h3(data["label"], class_="preview-label"),
        p(data["tagline"], class_="preview-tagline"),
        p(data["desc"], class_="preview-desc"),
        div(
            span(data["count"], class_="preview-count"),
            a(data["cta"], href=data["url"], class_="svc-btn"),
            class_="preview-foot",
        ),
        class_="preview-card reveal",
        data_delay=str(index * 120),
    )


def build_home_previews():
    previews = [
        HOME_KUNDEN_PREVIEW,
        HOME_TARIFE_PREVIEW,
        HOME_SOFTWARE_PREVIEW,
        HOME_OSS_PREVIEW,
        HOME_INFRA_PREVIEW,
    ]
    cards = [build_preview_card(p, i) for i, p in enumerate(previews)]
    return section(
        section_head(
            "01", "Was wir bauen",
            "Individuelle Websites für Kunden, Open-Source-Bibliotheken, kommerzielle "
            "Software und self-hosted Infrastruktur — aus einer Hand, mit dem gleichen "
            "Anspruch an Qualität.",
        ),
        div(*cards, class_="preview-grid"),
        class_="previews-section section-block", id="projekte",
    )


def build_stack():
    items = [
        div(
            div(span(s["name"], class_="stack-name"), span(s["role"], class_="stack-role"), class_="stack-info"),
            div(div(class_="stack-bar-fill", style=f"width:{s['bar']}%"), class_="stack-bar"),
            a("↗", href=s["url"], target="_blank", rel="noopener", class_="stack-link"),
            class_="stack-item reveal", data_delay=str(i * 70),
        )
        for i, s in enumerate(STACK)
    ]
    return section(
        section_head(
            "02", "Tech Stack",
            "Bewusst gewählt: open-source, self-hosted, kein Vendor-Lock-in. "
            "Jedes Tool hat einen konkreten Grund hier zu sein.",
        ),
        div(
            div(
                p("htmforge rendert diese Seite komplett in Python — kein Jinja, "
                  "kein Template-Ordner. Jede Section, jede Card, jeder Button "
                  "ist eine Python-Funktion.", class_="stack-prose reveal"),
                p("Flask bleibt bewusst dünn: nur Routes. Gunicorn als systemd-Service, "
                  "Cloudflare Tunnel ersetzt Nginx und SSL-Zertifikate vollständig.",
                  class_="stack-prose reveal", data_delay="100"),
                div(
                    span("KEIN NGINX",          class_="pill-tag"),
                    span("KEIN JINJA",           class_="pill-tag"),
                    span("KEIN CLOUD-ZWANG",     class_="pill-tag"),
                    class_="pill-row reveal", data_delay="200",
                ),
                class_="stack-left",
            ),
            div(*items, class_="stack-list"),
            class_="stack-split",
        ),
        class_="stack-section section-block", id="stack",
    )


def build_home(css_hash="", js_hash=""):
    page = html(
        _head(
            "NepiDesk — Websites für Kunden · Python · Open Source",
            "Freelance-Entwickler: individuelle Websites für Kunden, Python Web "
            "Development und self-hosted Open-Source-Tools.",
            css_hash,
        ),
        body(
            build_header("home"),
            main(
                build_hero(),
                build_ticker(),
                build_home_previews(),
                build_stack(),
                class_="page-main",
            ),
            build_footer(),
            div(id="toast-slot", class_="toast-slot"),
            script(src=f"/static/js/main.js?v={js_hash}", defer=True),
        ),
        lang="de",
    )
    return "<!DOCTYPE html>\n" + render(page)