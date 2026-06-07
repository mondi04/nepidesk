"""
NepiDesk — nepidesk.de
htmforge-Komponenten. Kein Flask, kein CSS, keine Logik.
"""

from htmforge import render
from htmforge.elements import (
    div, span, a, p, h1, h2, h3, nav, header, footer,
    main, section, iframe, script, link, meta,
    html, head, body, title, button, ul, li, raw, strong,
)
from htmforge.components.toast import Toast, ToastVariant

from data import (
    SITE_NAME, SITE_URL, SITE_AUTHOR,
    HERO_CLAIM, HERO_SUB,
    TICKER_ITEMS, PROJECTS, STACK,
    GRAFANA_BASE, GRAFANA_PANELS,
    SSH_PAGE, NAS_PAGE,
    HTMFORGE_VERSION,
)


# ── Atoms ────────────────────────────────────────────────

def tag_chip(tag: str):
    labels = {"oss": "OSS", "dev": "DEV", "sys": "SYS"}
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


# ── Header ───────────────────────────────────────────────

def build_header(active: str = "home"):
    nav_links = [
        ("home",    "/",          "Start"),
        ("tools",   "/#tools",    "Tools"),
        ("stack",   "/#stack",    "Stack"),
        ("htmforge","https://htmforge.nepidesk.de", "htmforge ↗"),
    ]
    nav_items = [
        a(
            label,
            href=href,
            class_=f"nav-link {'nav-active' if key == active else ''}",
            **({"target": "_blank", "rel": "noopener"} if href.startswith("http") else {}),
        )
        for key, href, label in nav_links
    ]
    return header(
        div(
            a(
                div(
                    span("ND", class_="logo-mark"),
                    div(
                        span("NepiDesk", class_="logo-name"),
                        span("software · security · oss", class_="logo-sub"),
                        class_="logo-text-block",
                    ),
                    class_="logo-inner",
                ),
                href="/", class_="logo",
            ),
            nav(*nav_items, class_="main-nav"),
            div(
                span("", class_="pulse-ring"),
                span("AVAILABLE", class_="online-text"),
                class_="header-right",
            ),
            class_="header-inner",
        ),
        class_="site-header",
    )


# ── Hero ─────────────────────────────────────────────────

def build_hero():
    return section(
        div(class_="parallax-grid", data_speed="0.3"),
        div(class_="parallax-glow parallax-glow-1", data_speed="0.5"),
        div(class_="parallax-glow parallax-glow-2", data_speed="0.2"),
        div(
            # Eyebrow
            div(
                span("", class_="eyebrow-dot"),
                span("Freelance · Remote · Worldwide", class_="eyebrow-text"),
                class_="eyebrow",
            ),
            # Logotype
            div(
                span("NEPI", class_="hero-word hero-word-1"),
                span("DESK", class_="hero-word hero-word-2"),
                class_="hero-logotype",
            ),
            # Claim
            p(HERO_CLAIM, class_="hero-claim"),
            p(HERO_SUB, class_="hero-sub"),
            # CTAs
            div(
                a("Projekte ansehen", href="/#tools", class_="cta-primary"),
                a("Kontakt", href="mailto:kontakt@nepidesk.de", class_="cta-secondary"),
                class_="hero-ctas",
            ),
            # HUD corners
            div(class_="hud-corner hud-tl"),
            div(class_="hud-corner hud-tr"),
            div(class_="hud-corner hud-bl"),
            div(class_="hud-corner hud-br"),
            class_="hero-box",
        ),
        class_="hero-section", id="hero",
    )


# ── Ticker ───────────────────────────────────────────────

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


# ── Projects ─────────────────────────────────────────────

def build_project_card(proj: dict, index: int):
    target_kwargs = {"target": "_blank", "rel": "noopener"} if proj["external"] else {}
    return div(
        div(
            span(proj["emoji"], class_="svc-icon"),
            div(
                tag_chip(proj["tag"]),
                span(proj["tagline"], class_="svc-tagline"),
                class_="svc-badges",
            ),
            class_="svc-top",
        ),
        h3(proj["label"], class_="svc-name"),
        p(proj["desc"], class_="svc-desc"),
        div(
            a(proj["cta"], href=proj["url"], class_="svc-btn", **target_kwargs),
            class_="svc-actions",
        ),
        class_="svc-card reveal",
        data_delay=str(index * 80),
    )


def build_projects():
    cards = [build_project_card(p, i) for i, p in enumerate(PROJECTS)]
    return section(
        section_head(
            "01", "Tools & Projekte",
            "Open-Source-Bibliotheken, self-hosted Dienste und interne Tools — "
            "gebaut mit dem gleichen Stack, dokumentiert damit andere davon lernen können.",
        ),
        div(*cards, class_="svc-grid"),
        class_="services-section section-block", id="tools",
    )


# ── Dashboard ────────────────────────────────────────────

def build_dashboard():
    def panel_url(pid): return f"{GRAFANA_BASE}&from=now-24h&to=now&panelId={pid}"

    def panel_cell(p):
        col = "panel-wide" if p["cols"] == 2 else "panel-single"
        return div(
            iframe(src=panel_url(p["id"]), loading="lazy",
                   class_="panel-frame", style=f"height:{p['height']}px"),
            span(p["label"], class_="panel-label"),
            class_=f"panel-cell {col} reveal",
        )

    panels = [panel_cell(p) for p in GRAFANA_PANELS]

    return section(
        section_head(
            "02", "Live Infrastructure",
            "Echtzeit-Metriken unserer Server-Infrastruktur — "
            "Prometheus + Grafana, fully self-hosted.",
        ),
        div(
            div(
                div(
                    div(span("STACK",   class_="info-key"), span("Prometheus + Node Exporter", class_="info-val"), class_="info-row reveal"),
                    div(span("REFRESH", class_="info-key"), span("1 Minute",                   class_="info-val"), class_="info-row reveal", data_delay="60"),
                    div(span("HOSTING", class_="info-key"), span("Self-hosted · kein Cloud",   class_="info-val"), class_="info-row reveal", data_delay="120"),
                    div(span("ACCESS",  class_="info-key"), span("Cloudflare Tunnel",          class_="info-val"), class_="info-row reveal", data_delay="180"),
                    div(span("STATUS",  class_="info-key"), span("Operational ✓",              class_="info-val info-green"), class_="info-row reveal", data_delay="240"),
                    class_="info-table",
                ),
                p(
                    "Zeigt wie wir Infrastruktur-Monitoring ohne Cloud-Abo und "
                    "ohne offene Ports realisieren — Grafana hinter einem Cloudflare Tunnel.",
                    class_="info-prose reveal", data_delay="300",
                ),
                class_="dashboard-info",
            ),
            div(*panels, class_="panels-grid"),
            class_="dashboard-split",
        ),
        class_="dashboard-section section-block", id="dashboard",
    )


# ── Stack ────────────────────────────────────────────────

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
            "03", "Tech Stack",
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


# ── Footer ───────────────────────────────────────────────

def build_footer():
    return footer(
        div(
            span("© 2025 NepiDesk · ", class_="dim"),
            span(SITE_AUTHOR, class_="dim"),
            span(" · ", class_="dim"),
            a("Impressum", href="/impressum", class_="footer-link"),
            class_="footer-left",
        ),
        div(
            span("Built with ", class_="dim"),
            a(f"htmforge v{HTMFORGE_VERSION}",
              href="https://pypi.org/project/htmforge/",
              target="_blank", class_="accent-link"),
            class_="footer-right",
        ),
        class_="site-footer",
    )


# ── Toast ────────────────────────────────────────────────

def build_toast_success():
    return Toast(message="✓ URL kopiert", variant=ToastVariant.SUCCESS, duration_ms=2500)


# ── Subpage shell ────────────────────────────────────────

def _subpage_shell(page_data: dict, content, css_hash="", js_hash=""):
    page = html(
        _head(page_data["title"] + " — NepiDesk", page_data["tagline"], css_hash),
        body(
            build_header(),
            main(
                section(
                    div(
                        a("← Zurück", href="/", class_="back-link"),
                        class_="subpage-back",
                    ),
                    div(
                        span("INTERN", class_="tag tag-sys"),
                        class_="subpage-eyebrow",
                    ),
                    h1(page_data["title"],   class_="subpage-title"),
                    p(page_data["tagline"],  class_="subpage-tagline"),
                    p(page_data["intro"],    class_="subpage-intro"),
                    class_="subpage-hero section-block",
                ),
                section(
                    div(
                        *[
                            div(
                                span(k, class_="how-key"),
                                p(v, class_="how-val"),
                                class_="how-row reveal", data_delay=str(i * 60),
                            )
                            for i, (k, v) in enumerate(page_data["how"])
                        ],
                        class_="how-grid",
                    ),
                    class_="subpage-how section-block",
                ),
                class_="page-main",
            ),
            build_footer(),
            div(id="toast-slot", class_="toast-slot"),
            script(src=f"/static/js/main.js?v={js_hash}", defer=True),
        ),
        lang="de",
    )
    return "<!DOCTYPE html>\n" + render(page)


# ── Head helper ──────────────────────────────────────────

def _head(page_title: str, description: str, css_hash: str = ""):
    return head(
        meta(charset="UTF-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1.0"),
        meta(name="description", content=description),
        meta(name="author",      content="Moritz · NepiDesk"),
        meta(property="og:title",       content=page_title),
        meta(property="og:description", content=description),
        meta(property="og:type",        content="website"),
        meta(property="og:url",         content=SITE_URL),
        title(page_title),
        link(rel="canonical", href=SITE_URL),
        link(rel="preconnect", href="https://fonts.googleapis.com"),
        link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        link(rel="stylesheet",
             href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=DM+Sans:wght@300;400;500&display=swap"),
        link(rel="stylesheet", href=f"/static/css/main.css?v={css_hash}"),
        script(src="https://unpkg.com/htmx.org@1.9.12", defer=True),
    )


# ── Full pages ───────────────────────────────────────────

def build_home(css_hash="", js_hash=""):
    page = html(
        _head(
            "NepiDesk — Python · Security · Open Source",
            "Freelance-Entwickler: Python Web Development, IT-Security, self-hosted Open-Source-Tools.",
            css_hash,
        ),
        body(
            build_header("home"),
            main(
                build_hero(),
                build_ticker(),
                build_projects(),
                build_dashboard(),
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


def build_ssh_page(css_hash="", js_hash=""):
    return _subpage_shell(SSH_PAGE, None, css_hash, js_hash)


def build_nas_page(css_hash="", js_hash=""):
    return _subpage_shell(NAS_PAGE, None, css_hash, js_hash)