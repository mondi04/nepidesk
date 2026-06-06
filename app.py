"""
belchenstrasse5.de — Home Dashboard
Built with htmforge v0.3.2
"""

from flask import Flask, Response
from htmforge import render
from htmforge.elements import (
    div, h1, h2, h3, p, a, span, iframe, section,
    nav, header, footer, main, ul, li, strong, raw,
    script, link, meta, style, html, head, body, title
)
from htmforge.components.badge import Badge, BadgeVariant
from htmforge.components.spinner import Spinner, SpinnerSize

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------

LINKS = [
    {
        "icon": "󰊢",  # nerd font git icon, fallback below
        "emoji": "📦",
        "label": "Gitea",
        "desc": "Code Repository & CI/CD",
        "url": "https://git.belchenstrasse5.de",
        "tag": "dev",
    },
    {
        "emoji": "✈️",
        "label": "Plane",
        "desc": "Projektstrukturierung vom Feinsten",
        "url": "https://plan.belchenstrasse5.de",
        "tag": "mgmt",
    },
    {
        "emoji": "🔐",
        "label": "SSH Access",
        "desc": "Terminale Zugriff auf den Server",
        "url": "https://ssh.belchenstrasse5.de",
        "tag": "sys",
    },
    {
        "emoji": "💾",
        "label": "NAS Storage",
        "desc": "Netzwerkspeicher & Backups",
        "url": "https://nas.belchenstrasse5.de",
        "tag": "sys",
    },
]

TAG_COLORS = {
    "dev":  ("dev",  "#3b82f6"),
    "mgmt": ("mgmt", "#a855f7"),
    "sys":  ("sys",  "#f59e0b"),
}

HTMFORGE_VERSION = "0.3.2"


# ---------------------------------------------------------------------------
# Component helpers
# ---------------------------------------------------------------------------

def build_tag_badge(tag: str):
    label, _ = TAG_COLORS.get(tag, (tag, "#888"))
    return span(label, class_=f"tag tag-{tag}")


def build_link_card(link_data: dict):
    tag = link_data.get("tag", "")
    return div(
        div(
            span(link_data["emoji"], class_="card-icon"),
            build_tag_badge(tag),
            class_="card-header",
        ),
        div(
            a(link_data["label"], href=link_data["url"],
              target="_blank", rel="noopener", class_="card-title"),
            p(link_data["desc"], class_="card-desc"),
            class_="card-body",
        ),
        div(
            span("→", class_="card-arrow"),
            class_="card-footer",
        ),
        class_="service-card",
    )


def build_page() -> str:
    cards = [build_link_card(lk) for lk in LINKS]

    spinner = Spinner(size=SpinnerSize.SM, label="Grafana lädt …")

    page_content = html(
        head(
            meta(charset="UTF-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1.0"),
            title("Belchenstraße 5 — Services"),
            link(rel="preconnect", href="https://fonts.googleapis.com"),
            link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
            link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Syne:wght@400;600;800&display=swap",
            ),
            style(raw(CSS)),
        ),
        body(
            # Animated grid background
            div(class_="bg-grid"),
            div(class_="bg-glow"),

            header(
                nav(
                    div(
                        span("⬡", class_="logo-hex"),
                        span("belchenstraße 5", class_="logo-text"),
                        class_="logo",
                    ),
                    div(
                        span("g7", class_="nav-chip"),
                        span("●", class_="status-dot"),
                        span("online", class_="status-text"),
                        class_="nav-status",
                    ),
                    class_="nav-inner",
                ),
                class_="site-header",
            ),

            main(
                # Hero
                section(
                    div(
                        h1(
                            span("Home", class_="hero-dim"),
                            raw("<br>"),
                            span("Lab", class_="hero-accent"),
                            class_="hero-title",
                        ),
                        p(
                            "Persönliche Infrastruktur — self-hosted, lokal, unter Kontrolle.",
                            class_="hero-sub",
                        ),
                        class_="hero-text",
                    ),
                    class_="hero",
                ),

                # Service Cards
                section(
                    h2("Services", class_="section-label"),
                    div(*cards, class_="cards-grid"),
                    class_="services-section",
                ),

                # Grafana
                section(
                    h2("System Dashboard", class_="section-label"),
                    div(
                        div(spinner, p("Dashboard wird geladen …", class_="loading-text"), class_="grafana-loading", id="grafana-loading"),
                        iframe(
                            src="https://monitoring.belchenstrasse5.de?kiosk=tv&viewPanel=0",
                            width="100%",
                            height="600",
                            loading="lazy",
                            onload="document.getElementById('grafana-loading').style.display='none'",
                            class_="grafana-frame",
                        ),
                        class_="grafana-wrapper",
                    ),
                    class_="dashboard-section",
                ),

                class_="page-main",
            ),

            footer(
                div(
                    span("Built with", class_="footer-dim"),
                    a(
                        f"htmforge v{HTMFORGE_VERSION}",
                        href="https://pypi.org/project/htmforge/",
                        target="_blank",
                        rel="noopener",
                        class_="footer-link",
                    ),
                    span("·", class_="footer-dim"),
                    span("Moritz, 2025", class_="footer-dim"),
                    class_="footer-inner",
                ),
                class_="site-footer",
            ),

            script(raw(JS)),
        ),
        lang="de",
    )

    return "<!DOCTYPE html>\n" + render(page_content)


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

CSS = """
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:        #0b0d11;
  --surface:   #12151c;
  --border:    #1e2330;
  --border-hi: #2d3448;
  --text:      #e2e6f0;
  --dim:       #6b7592;
  --accent:    #5affa3;
  --accent2:   #3b82f6;
  --mono:      'JetBrains Mono', monospace;
  --sans:      'Syne', sans-serif;
  --radius:    12px;
  --radius-sm: 6px;
}

html { scroll-behavior: smooth; }

body {
  font-family: var(--sans);
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  overflow-x: hidden;
}

/* Background */
.bg-grid {
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background-image:
    linear-gradient(rgba(90,255,163,.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(90,255,163,.03) 1px, transparent 1px);
  background-size: 40px 40px;
}
.bg-glow {
  position: fixed; inset: 0; pointer-events: none; z-index: 0;
  background: radial-gradient(ellipse 60% 50% at 20% 10%, rgba(90,255,163,.06) 0%, transparent 70%),
              radial-gradient(ellipse 40% 40% at 80% 80%, rgba(59,130,246,.05) 0%, transparent 70%);
}

/* Header */
.site-header {
  position: sticky; top: 0; z-index: 100;
  border-bottom: 1px solid var(--border);
  background: rgba(11,13,17,.85);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
}
.nav-inner {
  max-width: 1100px; margin: 0 auto;
  padding: 16px 24px;
  display: flex; align-items: center; justify-content: space-between;
}
.logo { display: flex; align-items: center; gap: 10px; }
.logo-hex {
  font-size: 24px; color: var(--accent);
  animation: pulse-hex 3s ease-in-out infinite;
}
@keyframes pulse-hex {
  0%,100% { opacity: 1; text-shadow: 0 0 0 transparent; }
  50%      { opacity: .7; text-shadow: 0 0 12px var(--accent); }
}
.logo-text {
  font-family: var(--mono); font-size: 14px;
  color: var(--dim); letter-spacing: .05em;
}
.nav-status {
  display: flex; align-items: center; gap: 8px;
  font-family: var(--mono); font-size: 12px;
}
.nav-chip {
  background: var(--surface); border: 1px solid var(--border);
  padding: 3px 10px; border-radius: 999px; color: var(--dim);
}
.status-dot {
  color: var(--accent); font-size: 10px;
  animation: blink 2s step-end infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:.2} }
.status-text { color: var(--accent); font-size: 12px; }

/* Main */
.page-main { position: relative; z-index: 1; max-width: 1100px; margin: 0 auto; padding: 0 24px 80px; }

/* Hero */
.hero { padding: 80px 0 60px; }
.hero-title {
  font-size: clamp(56px, 10vw, 112px);
  font-weight: 800; line-height: .95;
  letter-spacing: -.04em;
}
.hero-dim   { color: var(--dim); }
.hero-accent { color: var(--accent); }
.hero-sub {
  margin-top: 24px;
  font-family: var(--mono); font-size: 14px;
  color: var(--dim); max-width: 420px; line-height: 1.7;
}

/* Section label */
.section-label {
  font-family: var(--mono); font-size: 11px;
  color: var(--dim); letter-spacing: .15em;
  text-transform: uppercase;
  margin-bottom: 24px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
}

/* Cards */
.services-section { margin-bottom: 72px; }
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 16px;
}

.service-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  display: flex; flex-direction: column; gap: 16px;
  cursor: pointer;
  transition: border-color .2s, transform .2s, box-shadow .2s;
  position: relative; overflow: hidden;
}
.service-card::before {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(90,255,163,.04), transparent 60%);
  opacity: 0; transition: opacity .2s;
}
.service-card:hover {
  border-color: var(--border-hi);
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(0,0,0,.4), 0 0 0 1px rgba(90,255,163,.08);
}
.service-card:hover::before { opacity: 1; }

.card-header { display: flex; align-items: center; justify-content: space-between; }
.card-icon { font-size: 28px; line-height: 1; }
.card-body { flex: 1; }
.card-title {
  font-family: var(--sans); font-weight: 600; font-size: 18px;
  color: var(--text); text-decoration: none;
  display: block; margin-bottom: 6px;
  transition: color .15s;
}
.service-card:hover .card-title { color: var(--accent); }
.card-desc { font-family: var(--mono); font-size: 12px; color: var(--dim); line-height: 1.6; }
.card-footer { display: flex; justify-content: flex-end; }
.card-arrow {
  font-size: 18px; color: var(--border-hi);
  transition: color .2s, transform .2s;
}
.service-card:hover .card-arrow { color: var(--accent); transform: translateX(4px); }

/* Tags */
.tag {
  font-family: var(--mono); font-size: 10px;
  padding: 3px 8px; border-radius: var(--radius-sm);
  letter-spacing: .08em; text-transform: uppercase;
}
.tag-dev  { background: rgba(59,130,246,.15); color: #93c5fd; border: 1px solid rgba(59,130,246,.2); }
.tag-mgmt { background: rgba(168,85,247,.15); color: #d8b4fe; border: 1px solid rgba(168,85,247,.2); }
.tag-sys  { background: rgba(245,158,11,.15);  color: #fcd34d; border: 1px solid rgba(245,158,11,.2); }

/* Grafana */
.dashboard-section { margin-bottom: 72px; }
.grafana-wrapper {
  position: relative;
  border: 1px solid var(--border); border-radius: var(--radius); overflow: hidden;
}
.grafana-loading {
  display: flex; align-items: center; gap: 12px;
  padding: 20px 24px;
  background: var(--surface);
  font-family: var(--mono); font-size: 13px;
  color: var(--dim);
}
.spinner {
  width: 16px; height: 16px;
  border: 2px solid var(--border-hi);
  border-top-color: var(--accent);
  border-radius: 50%;
  animation: spin .7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
.loading-text { color: var(--dim); }
.grafana-frame { display: block; border: none; }

/* Footer */
.site-footer {
  border-top: 1px solid var(--border);
  padding: 24px;
  position: relative; z-index: 1;
}
.footer-inner {
  max-width: 1100px; margin: 0 auto;
  display: flex; align-items: center; gap: 12px;
  font-family: var(--mono); font-size: 12px;
}
.footer-dim { color: var(--dim); }
.footer-link {
  color: var(--accent); text-decoration: none;
  transition: opacity .15s;
}
.footer-link:hover { opacity: .7; }

/* Entrance animations */
.hero         { animation: fade-up .6s ease both; }
.service-card { animation: fade-up .5s ease both; }
.service-card:nth-child(1) { animation-delay: .05s; }
.service-card:nth-child(2) { animation-delay: .10s; }
.service-card:nth-child(3) { animation-delay: .15s; }
.service-card:nth-child(4) { animation-delay: .20s; }
@keyframes fade-up {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
"""

# ---------------------------------------------------------------------------
# JS
# ---------------------------------------------------------------------------

JS = """
// Make entire card clickable
document.querySelectorAll('.service-card').forEach(card => {
  const link = card.querySelector('.card-title');
  if (link) {
    card.addEventListener('click', e => {
      if (e.target !== link) window.open(link.href, '_blank', 'noopener');
    });
  }
});
"""


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return Response(build_page(), mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)