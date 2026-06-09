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
    TICKER_ITEMS, STACK,
    GRAFANA_BASE, GRAFANA_PANELS, INFRA_INFO,
    SSH_PAGE, NAS_PAGE,
    HTMFORGE_VERSION,
    IMPRESSUM, DATENSCHUTZ,
    HOME_OSS_PREVIEW, HOME_SOFTWARE_PREVIEW, HOME_INFRA_PREVIEW,
    OSS_PROJECTS,
    SOFTWARE_COMING_SOON,
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
        ("home",        "/",            "Start"),
        ("opensource",  "/opensource",  "Open Source"),
        ("software",    "/software",    "Software"),
        ("infra",       "/infra",       "Infra"),
    ]
    nav_items = [
        a(
            label,
            href=href,
            class_=f"nav-link {'nav-active' if key == active else ''}",
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
            div(
                span("", class_="eyebrow-dot"),
                span("Freelance · Remote · Worldwide", class_="eyebrow-text"),
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
                a("Projekte ansehen", href="/opensource", class_="cta-primary"),
                a("Kontakt", href="mailto:kontakt@nepidesk.de", class_="cta-secondary"),
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


# ── Home Preview Cards ────────────────────────────────────

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
    previews = [HOME_OSS_PREVIEW, HOME_SOFTWARE_PREVIEW, HOME_INFRA_PREVIEW]
    cards = [build_preview_card(p, i) for i, p in enumerate(previews)]
    return section(
        section_head(
            "01", "Was wir bauen",
            "Open-Source-Bibliotheken, kommerzielle Software und self-hosted Infrastruktur — "
            "aus einer Hand, mit dem gleichen Anspruch an Qualität.",
        ),
        div(*cards, class_="preview-grid"),
        class_="previews-section section-block", id="projekte",
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


# ── Footer ───────────────────────────────────────────────

def build_footer():
    return footer(
        div(
            span("© 2025 NepiDesk · ", class_="dim"),
            span(SITE_AUTHOR, class_="dim"),
            class_="footer-left",
        ),
        div(
            a("Impressum", href="/impressum", class_="footer-link"),
            span(" · ", class_="dim"),
            a("Datenschutz", href="/datenschutz", class_="footer-link"),
            class_="footer-center",
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


# ── Head helper ──────────────────────────────────────────

def _head(page_title: str, description: str, css_hash: str = "", canonical: str = SITE_URL):
    json_ld = """{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Moritz Mond",
  "url": "https://nepidesk.de",
  "jobTitle": "Freelance Developer",
  "description": "Freelance-Entwickler mit Fokus auf Python Web Development, IT-Security und self-hosted Open-Source-Tools.",
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
        meta(property="og:image:alt",    content="NepiDesk - Python · Security · Open Source"),
        meta(name="twitter:image",       content=SITE_URL + "/static/og-image.png"),
        meta(name="twitter:card",        content="summary_large_image"),
        meta(name="twitter:title",       content=page_title),
        meta(name="twitter:description", content=description),
        title(page_title),
        link(rel="canonical", href=canonical),
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


# ── OSS Page ─────────────────────────────────────────────

def _oss_project_card(proj: dict, index: int):
    meta_rows = [
        div(
            span(k, class_="meta-key"),
            span(v, class_="meta-val"),
            class_="meta-row",
        )
        for k, v in proj["meta"]
    ]
    link_btns = [
        a(
            lnk["label"],
            href=lnk["url"],
            target="_blank", rel="noopener",
            class_=f"svc-btn {'svc-btn-secondary' if not lnk['primary'] else ''}",
        )
        for lnk in proj["links"]
    ]
    return div(
        div(
            span(proj["emoji"], class_="oss-icon"),
            div(
                tag_chip(proj["tag"]),
                span(proj["tagline"], class_="svc-tagline"),
                class_="svc-badges",
            ),
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


# ── Software Page ─────────────────────────────────────────

def build_software_page(css_hash="", js_hash=""):
    cs = SOFTWARE_COMING_SOON
    teaser_cards = [
        div(
            span(t["emoji"], class_="teaser-icon"),
            h3(t["label"], class_="teaser-label"),
            p(t["desc"], class_="teaser-desc"),
            span(t["status"], class_="teaser-status"),
            class_="teaser-card reveal",
            data_delay=str(i * 100),
        )
        for i, t in enumerate(cs["teaser"])
    ]
    content = [
        section(
            section_head("01", cs["title"], cs["intro"]),
            # Coming Soon Banner
            div(
                div(
                    span("🚧", class_="coming-emoji"),
                    h2("Coming Soon", class_="coming-title"),
                    p(
                        "Software-Projekte werden hier dokumentiert sobald sie "
                        "öffentlich verfügbar sind. Aktuell in aktiver Entwicklung.",
                        class_="coming-sub",
                    ),
                    class_="coming-inner",
                ),
                class_="coming-banner reveal",
            ),
            div(*teaser_cards, class_="teaser-grid"),
            class_="section-block",
        ),
    ]
    return _page_shell(
        "Software", "Kommerzielle und interne Software-Projekte von NepiDesk.",
        "software", content, css_hash, js_hash,
        canonical=SITE_URL + "/software",
    )


# ── Infra Page ────────────────────────────────────────────

def build_infra_page(css_hash="", js_hash=""):
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

    info_rows = [
        div(
            span(k, class_="info-key"),
            span(v, class_="info-val" + (" info-green" if k == "STATUS" else "")),
            class_="info-row reveal",
            data_delay=str(i * 60),
        )
        for i, (k, v) in enumerate(INFRA_INFO)
    ]

    content = [
        section(
            section_head(
                "01", "Live Infrastructure",
                "Echtzeit-Metriken unserer Server-Infrastruktur — "
                "Prometheus + Grafana, fully self-hosted.",
            ),
            div(
                div(
                    div(*info_rows, class_="info-table"),
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
            class_="section-block",
        ),
    ]
    return _page_shell(
        "Infra", "Live-Monitoring der NepiDesk Infrastruktur — Prometheus, Grafana, self-hosted.",
        "infra", content, css_hash, js_hash,
        canonical=SITE_URL + "/infra",
    )


# ── Subpage shell (SSH, NAS) ──────────────────────────────

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


# ── Impressum ────────────────────────────────────────────

def build_impressum_page(css_hash="", js_hash=""):
    imp = IMPRESSUM

    def row(label: str, *children):
        return div(
            span(label, class_="legal-key"),
            div(*children, class_="legal-val"),
            class_="legal-row",
        )

    content = [
        section(
            div(
                a("← Zurück", href="/", class_="back-link"),
                class_="subpage-back",
            ),
            h1("Impressum", class_="legal-page-title"),
            p("Angaben gemäß § 5 TMG", class_="legal-subtitle"),

            # Verantwortlicher
            div(
                h2("Verantwortlicher", class_="legal-section-title"),
                row("Name",         span(imp["name"],       class_="legal-text")),
                row("Anschrift",    span(imp["strasse"],    class_="legal-text"),
                                    span(imp["ort"],        class_="legal-text")),
                row("Rechtsform",   span(imp["rechtsform"], class_="legal-text")),
                row("E-Mail",       a(imp["email"], href=f"mailto:{imp['email']}", class_="legal-link")),
                class_="legal-block",
            ),

            # Hinweis Steuernummer
            div(
                h2("Steuerliche Angaben", class_="legal-section-title"),
                p(
                    "Eine Umsatzsteuer-Identifikationsnummer liegt derzeit nicht vor. "
                    "Umsatzsteuerbefreiung gemäß § 19 UStG (Kleinunternehmerregelung) "
                    "wird bei Bedarf separat kommuniziert.",
                    class_="legal-prose",
                ),
                class_="legal-block",
            ),

            # Streitschlichtung
            div(
                h2("Streitschlichtung", class_="legal-section-title"),
                p(
                    "Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: ",
                    a("https://ec.europa.eu/consumers/odr",
                      href="https://ec.europa.eu/consumers/odr",
                      target="_blank", rel="noopener", class_="legal-link"),
                    span(". Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren "
                         "vor einer Verbraucherschlichtungsstelle teilzunehmen."),
                    class_="legal-prose",
                ),
                class_="legal-block",
            ),

            # Haftung
            div(
                h2("Haftung für Inhalte", class_="legal-section-title"),
                p(
                    "Als Diensteanbieter sind wir gemäß § 7 Abs. 1 TMG für eigene Inhalte auf diesen Seiten "
                    "nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als "
                    "Diensteanbieter jedoch nicht verpflichtet, übermittelte oder gespeicherte fremde "
                    "Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige "
                    "Tätigkeit hinweisen.",
                    class_="legal-prose",
                ),
                class_="legal-block",
            ),

            class_="legal-page section-block",
        ),
    ]
    return _page_shell(
        "Impressum", "Impressum — NepiDesk",
        "", content, css_hash, js_hash,
        canonical=SITE_URL + "/impressum",
    )


# ── Datenschutz ──────────────────────────────────────────

def build_datenschutz_page(css_hash="", js_hash=""):
    ds = DATENSCHUTZ

    def block(title: str, *paras):
        return div(
            h2(title, class_="legal-section-title"),
            *[p(text, class_="legal-prose") for text in paras],
            class_="legal-block",
        )

    content = [
        section(
            div(
                a("← Zurück", href="/", class_="back-link"),
                class_="subpage-back",
            ),
            h1("Datenschutzerklärung", class_="legal-page-title"),
            p("Zuletzt aktualisiert: Juni 2025", class_="legal-subtitle"),

            block(
                "1. Verantwortlicher",
                f"Verantwortlich im Sinne der DSGVO: {ds['verantwortlicher_name']}, "
                f"erreichbar unter {ds['verantwortlicher_email']}.",
            ),

            block(
                "2. Welche Daten wir erheben",
                "Diese Website erhebt keine personenbezogenen Daten durch Tracking, "
                "Cookies oder Analyse-Tools. Es werden keine Cookies gesetzt.",
                "Beim Aufruf der Website werden durch den Webserver technisch notwendige "
                "Server-Logs gespeichert (IP-Adresse, Zeitstempel, aufgerufene URL, "
                "HTTP-Statuscode, verwendeter Browser). Diese Daten dienen ausschließlich "
                "der technischen Fehlerdiagnose und werden nach spätestens 7 Tagen gelöscht.",
            ),

            block(
                "3. Hosting & Infrastruktur",
                f"Die Website wird auf einem eigenen, privat betriebenen Server in Deutschland gehostet. "
                "Es werden keine externen Hosting-Anbieter eingesetzt.",
                "Der Datenverkehr wird über Cloudflare (Cloudflare, Inc., 101 Townsend St., "
                "San Francisco, CA 94107, USA) geleitet. Cloudflare agiert dabei als "
                "Reverse-Proxy und kann dabei technische Metadaten (IP-Adresse, Request-Header) "
                "verarbeiten. Die eigentliche IP-Adresse des Servers wird dabei nicht öffentlich "
                "exponiert. Weitere Informationen: https://www.cloudflare.com/privacypolicy/",
            ),

            block(
                "4. Kontaktaufnahme per E-Mail",
                "Wenn Sie uns per E-Mail kontaktieren, werden die von Ihnen übermittelten Daten "
                "(E-Mail-Adresse, ggf. Name und Nachrichteninhalt) ausschließlich zur Bearbeitung "
                "Ihrer Anfrage verwendet. Diese Daten werden nicht an Dritte weitergegeben und "
                "nach Abschluss der Anfrage gelöscht, sofern keine gesetzlichen Aufbewahrungsfristen bestehen.",
            ),

            block(
                "5. Ihre Rechte",
                "Sie haben jederzeit das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16 DSGVO), "
                "Löschung (Art. 17 DSGVO), Einschränkung der Verarbeitung (Art. 18 DSGVO) sowie "
                "Datenübertragbarkeit (Art. 20 DSGVO).",
                "Zur Ausübung Ihrer Rechte genügt eine E-Mail an kontakt@nepidesk.de. "
                "Sie haben zudem das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.",
            ),

            block(
                "6. Externe Links",
                "Diese Website enthält Links zu externen Websites (z. B. PyPI, GitHub, Cloudflare). "
                "Für die Datenschutzpraktiken dieser externen Anbieter übernehmen wir keine Verantwortung.",
            ),

            block(
                "7. Aktualität",
                "Wir behalten uns vor, diese Datenschutzerklärung bei Bedarf anzupassen, "
                "etwa bei technischen Änderungen der Website oder neuen gesetzlichen Anforderungen.",
            ),

            class_="legal-page section-block",
        ),
    ]
    return _page_shell(
        "Datenschutz", "Datenschutzerklärung — NepiDesk",
        "", content, css_hash, js_hash,
        canonical=SITE_URL + "/datenschutz"
    )