"""
components/infra.py
Live-Infrastruktur-Dashboard. GRAFANA_BASE kommt bewusst aus config.py / .env —
sonst steht die interne Grafana-URL im öffentlichen GitHub-Repo.
"""

from htmforge.elements import div, span, p, iframe, section

from data import SITE_URL, GRAFANA_PANELS, INFRA_INFO
from config import GRAFANA_BASE
from .shared import section_head, _page_shell


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