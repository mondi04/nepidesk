"""
htmforge-Komponenten für belchenstrasse5.de
Kein Flask, kein CSS, keine Business-Logik — nur Komponenten.
"""

from htmforge import render
from htmforge.elements import (
    div, span, a, p, h1, h2, h3, nav, header, footer,
    main, section, iframe, script, link, meta, style,
    html, head, body, title, button, ul, li, raw, strong,
)
from htmforge.components.spinner import Spinner, SpinnerSize
from htmforge.components.tabs import Tabs
from htmforge.components.badge import Badge, BadgeVariant
from htmforge.components.toast import Toast, ToastVariant

from data import SERVICES, SERVER_SPECS, STACK, HTMFORGE_VERSION, SITE_OWNER, GRAFANA_URL


# ---------------------------------------------------------------------------
# Atoms
# ---------------------------------------------------------------------------

def status_pill(status: str):
    return span(
        span("", class_=f"pip pip-{status}"),
        status,
        class_=f"status-pill status-{status}",
    )


def tag_badge(tag: str):
    return span(tag, class_=f"tag tag-{tag}")


def hud_label(text: str):
    return span(text, class_="hud-label")


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

def build_header():
    return header(
        div(
            # Logo
            a(
                div(
                    span("ND", class_="logo-mark"),
                    div(
                        span("NepiDesk", class_="logo-name"),
                        span("/ belchenstraße 5", class_="logo-sub"),
                        class_="logo-text-block",
                    ),
                    class_="logo-inner",
                ),
                href="/",
                class_="logo",
            ),
            # Nav center — HUD status
            div(
                span("SYS", class_="hud-key"),
                span("NOMINAL", class_="hud-val hud-green"),
                span("·", class_="hud-sep"),
                span("HOST", class_="hud-key"),
                span("g7", class_="hud-val"),
                span("·", class_="hud-sep"),
                span("NET", class_="hud-key"),
                span("CF-TUNNEL", class_="hud-val hud-blue"),
                class_="hud-strip",
            ),
            # Right
            div(
                span("", class_="pulse-ring"),
                span("ONLINE", class_="online-text"),
                class_="header-right",
            ),
            class_="header-inner",
        ),
        class_="site-header",
    )


# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------

def build_hero():
    return section(
        # Parallax layers (controlled by JS)
        div(class_="parallax-grid", data_speed="0.3"),
        div(class_="parallax-glow parallax-glow-1", data_speed="0.5"),
        div(class_="parallax-glow parallax-glow-2", data_speed="0.2"),

        div(
            div(
                span("NEPI", class_="hero-word hero-word-1"),
                span("DESK", class_="hero-word hero-word-2"),
                class_="hero-logotype",
            ),
            p(
                "Persönliche Infrastruktur — self-hosted, lokal, unter Kontrolle.",
                raw("<br>"),
                span("Gebaut mit ", class_="dim"),
                a("htmforge", href="https://pypi.org/project/htmforge/",
                  target="_blank", class_="accent-link"),
                span(f" v{HTMFORGE_VERSION} — kein Template, nur Python.", class_="dim"),
                class_="hero-sub",
            ),
            # HUD corners
            div(class_="hud-corner hud-tl"),
            div(class_="hud-corner hud-tr"),
            div(class_="hud-corner hud-bl"),
            div(class_="hud-corner hud-br"),
            class_="hero-box",
        ),
        class_="hero-section",
        id="hero",
    )


# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------

def build_service_card(svc: dict, index: int):
    return div(
        div(
            span(svc["emoji"], class_="svc-icon"),
            div(
                tag_badge(svc["tag"]),
                status_pill(svc["status"]),
                class_="svc-badges",
            ),
            class_="svc-top",
        ),
        h3(svc["label"], class_="svc-name"),
        p(svc["desc"], class_="svc-desc"),
        div(
            a("Öffnen →", href=svc["url"], target="_blank",
              rel="noopener", class_="svc-btn"),
            button("Kopieren",
                   class_="svc-copy",
                   data_url=svc["url"],
                   hx_get="/toast/copy",
                   hx_target="#toast-slot",
                   hx_swap="innerHTML"),
            class_="svc-actions",
        ),
        class_="svc-card reveal",
        data_delay=str(index * 80),
    )


def build_services():
    cards = [build_service_card(s, i) for i, s in enumerate(SERVICES)]
    return section(
        div(
            span("01", class_="section-num"),
            h2("Services", class_="section-title"),
            class_="section-head",
        ),
        div(*cards, class_="svc-grid"),
        class_="services-section section-block",
        id="services",
    )


# ---------------------------------------------------------------------------
# Server specs ticker
# ---------------------------------------------------------------------------

def build_specs_ticker():
    items = []
    for spec in SERVER_SPECS:
        items.append(
            div(
                span(spec["key"], class_="spec-key"),
                span(spec["value"], class_="spec-val"),
                span(spec["detail"], class_="spec-detail"),
                class_="spec-item",
            )
        )
    # duplicate for infinite scroll
    items_dup = items + [
        div(
            span(spec["key"], class_="spec-key"),
            span(spec["value"], class_="spec-val"),
            span(spec["detail"], class_="spec-detail"),
            class_="spec-item",
        )
        for spec in SERVER_SPECS
    ]
    return div(
        div(*items_dup, class_="ticker-track"),
        class_="specs-ticker reveal",
    )


# ---------------------------------------------------------------------------
# Grafana
# ---------------------------------------------------------------------------

def build_dashboard():
    spinner = Spinner(size=SpinnerSize.MD, label="Grafana lädt …")
    return section(
        div(
            span("02", class_="section-num"),
            h2("System Dashboard", class_="section-title"),
            class_="section-head",
        ),
        div(
            div(spinner, p("Dashboard wird geladen …", class_="loading-hint"), class_="grafana-loading", id="grafana-loading"),
            iframe(
                src=GRAFANA_URL,
                loading="lazy",
                onload="document.getElementById('grafana-loading').style.display='none'",
                class_="grafana-frame",
            ),
            class_="grafana-wrap reveal",
        ),
        class_="dashboard-section section-block",
        id="dashboard",
    )


# ---------------------------------------------------------------------------
# Stack
# ---------------------------------------------------------------------------

def build_stack():
    items = [
        div(
            span(s["name"], class_="stack-name"),
            span(s["role"], class_="stack-role"),
            a("↗", href=s["url"], target="_blank", class_="stack-link"),
            class_="stack-item reveal",
            data_delay=str(i * 60),
        )
        for i, s in enumerate(STACK)
    ]
    return section(
        div(
            span("03", class_="section-num"),
            h2("Stack", class_="section-title"),
            class_="section-head",
        ),
        div(*items, class_="stack-list"),
        class_="stack-section section-block",
        id="stack",
    )


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

def build_footer():
    return footer(
        div(
            span("Built with ", class_="dim"),
            a(f"htmforge v{HTMFORGE_VERSION}",
              href="https://pypi.org/project/htmforge/",
              target="_blank", class_="accent-link"),
            span(" — ", class_="dim"),
            span(SITE_OWNER, class_="dim"),
            class_="footer-left",
        ),
        div(
            span("Kein Template. Kein Jinja. Nur Python.", class_="footer-motto"),
            class_="footer-right",
        ),
        class_="site-footer",
    )


# ---------------------------------------------------------------------------
# Toast
# ---------------------------------------------------------------------------

def build_toast_success():
    return Toast(message="✓ URL in Zwischenablage", variant=ToastVariant.SUCCESS, duration_ms=2500)


# ---------------------------------------------------------------------------
# Full page
# ---------------------------------------------------------------------------

def build_page(css_hash: str = "", js_hash: str = "") -> str:
    page = html(
        head(
            meta(charset="UTF-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            meta(name="description", content="NepiDesk — persönliche Infrastruktur, gebaut mit htmforge"),
            title("NepiDesk · Belchenstraße 5"),
            link(rel="preconnect", href="https://fonts.googleapis.com"),
            link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
            link(rel="stylesheet",
                 href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap"),
            link(rel="stylesheet", href=f"/static/css/main.css?v={css_hash}"),
            script(src="https://unpkg.com/htmx.org@1.9.12", defer=True),
        ),
        body(
            build_header(),
            main(
                build_hero(),
                build_specs_ticker(),
                build_services(),
                build_dashboard(),
                build_stack(),
                class_="page-main",
            ),
            build_footer(),
            # Toast slot
            div(id="toast-slot", class_="toast-slot"),
            script(src=f"/static/js/main.js?v={js_hash}", defer=True),
        ),
        lang="de",
    )
    return "<!DOCTYPE html>\n" + render(page)