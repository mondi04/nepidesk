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

from data import SERVICES, SERVER_SPECS, STACK, HTMFORGE_VERSION, SITE_OWNER, GRAFANA_BASE, GRAFANA_PANELS


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
        section_head(
            "01",
            "Services",
            "Alle laufenden Dienste auf g7 — self-hosted, passwortgeschützt, "
            "über Cloudflare Tunnel erreichbar. Kein offener Port, kein Nginx.",
        ),
        div(*cards, class_="svc-grid"),
        class_="services-section section-block",
        id="services",
    )


# ---------------------------------------------------------------------------
# Server specs ticker
# ---------------------------------------------------------------------------

def build_specs_ticker():
    def make_items():
        return [
            div(
                span(spec["key"],    class_="spec-key"),
                span(spec["value"],  class_="spec-val"),
                span(spec["detail"], class_="spec-detail"),
                class_="spec-item",
            )
            for spec in SERVER_SPECS
        ]
    # 4× wiederholen damit der Loop auf jeder Bildschirmbreite nahtlos ist
    all_items = make_items() + make_items() + make_items() + make_items()
    return div(
        div(*all_items, class_="ticker-track"),
        class_="specs-ticker",
    )


# ---------------------------------------------------------------------------
# Section header with typewriter
# ---------------------------------------------------------------------------

def section_head(num: str, title: str, subtitle: str = ""):
    """Gibt einen Section-Header zurück. Der Titel bekommt data-typewriter,
    JS tippt ihn Zeichen für Zeichen wenn er ins Viewport kommt."""
    return div(
        div(
            span(num, class_="section-num"),
            span("·", class_="section-dot"),
            class_="section-meta",
        ),
        h2(
            span("", class_="typewriter-text"),
            span("▌", class_="typewriter-cursor"),
            data_typewriter=title,
            class_="section-title typewriter",
        ),
        p(subtitle, class_="section-sub") if subtitle else span(""),
        class_="section-head",
    )


# ---------------------------------------------------------------------------
# Grafana
# ---------------------------------------------------------------------------

def build_dashboard():
    # Dynamische from/to: jetzt bis jetzt-24h (ms timestamps)
    # Flask/Python berechnet das zur Laufzeit im build_page() Aufruf —
    # hier bauen wir die Panels mit einem JS-snippet das die URLs patcht.
    # Einfacher: wir nutzen Grafanas "now-24h" relative Zeit via URL-Param.
    def panel_url(panel_id: str) -> str:
        return (
            GRAFANA_BASE
            + f"&from=now-24h&to=now"
            + f"&panelId={panel_id}"
        )

    def panel_iframe(p: dict):
        col_class = "panel-wide" if p["cols"] == 2 else "panel-single"
        return div(
            iframe(
                src=panel_url(p["id"]),
                loading="lazy",
                class_="panel-frame",
                style=f"height:{p['height']}px",
            ),
            span(p["label"], class_="panel-label"),
            class_=f"panel-cell {col_class} reveal",
        )

    panels = [panel_iframe(p) for p in GRAFANA_PANELS]

    return section(
        section_head(
            "02",
            "System Dashboard",
            "Live-Metriken von g7 — Prometheus + Node Exporter via Grafana. "
            "CPU, RAM, Disk I/O, Netzwerktraffic — alles in Echtzeit.",
        ),
        div(
            # Left info
            div(
                div(
                    div(span("HOST",   class_="info-key"), span("g7 · Ubuntu 22.04",             class_="info-val"), class_="info-row reveal"),
                    div(span("RAM",    class_="info-key"), span("16 GB DDR3",                     class_="info-val"), class_="info-row reveal", data_delay="60"),
                    div(span("STACK",  class_="info-key"), span("Prometheus + Node Exporter",     class_="info-val"), class_="info-row reveal", data_delay="120"),
                    div(span("TUNNEL", class_="info-key"), span("Cloudflare — kein offener Port", class_="info-val"), class_="info-row reveal", data_delay="180"),
                    div(span("UPDATE", class_="info-key"), span("Echtzeit · 1m Refresh",         class_="info-val info-green"), class_="info-row reveal", data_delay="240"),
                    class_="info-table",
                ),
                p(
                    "Das Dashboard läuft vollständig self-hosted. Kein Cloud-Abo, "
                    "keine externen Services — nur g7, Grafana und ein Cloudflare Tunnel.",
                    class_="info-prose reveal", data_delay="300",
                ),
                class_="dashboard-info",
            ),
            # Right panel grid
            div(*panels, class_="panels-grid"),
            class_="dashboard-split",
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
            div(
                span(s["name"], class_="stack-name"),
                span(s["role"], class_="stack-role"),
                class_="stack-info",
            ),
            # Animated bar
            div(
                div(class_="stack-bar-fill", style=f"width:{s.get('bar', 90)}%"),
                class_="stack-bar",
            ),
            a("↗", href=s["url"], target="_blank", rel="noopener", class_="stack-link"),
            class_="stack-item reveal",
            data_delay=str(i * 70),
        )
        for i, s in enumerate(STACK)
    ]

    return section(
        section_head(
            "03",
            "Tech Stack",
            "Die Werkzeuge hinter belchenstrasse5.de — und hinter NepiDesk. "
            "Jedes Tool ist bewusst gewählt: self-hosted, open-source, kein Vendor-Lock-in.",
        ),
        # Split: Erklärtext links, Stack-Liste rechts
        div(
            # Left — prose
            div(
                p(
                    "htmforge übernimmt das komplette HTML-Rendering in Python — "
                    "kein Jinja, kein Template-Ordner. Was du hier siehst, wurde "
                    "Zeile für Zeile in Python gebaut.",
                    class_="stack-prose reveal",
                ),
                p(
                    "Flask ist bewusst dünn gehalten: nur Routes, kein Business-Logik. "
                    "Gunicorn läuft als systemd-Service, Cloudflare Tunnel ersetzt "
                    "Nginx und SSL komplett.",
                    class_="stack-prose reveal", data_delay="100",
                ),
                div(
                    span("KEIN NGINX", class_="pill-tag"),
                    span("KEIN SSL-ZERTIFIKAT", class_="pill-tag"),
                    span("KEIN JINJA", class_="pill-tag"),
                    class_="pill-row reveal", data_delay="200",
                ),
                class_="stack-left",
            ),
            # Right — list
            div(*items, class_="stack-list"),
            class_="stack-split",
        ),
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