"""
components/software.py
"""

from htmforge.elements import div, span, h2, h3, p, section

from data import SITE_URL, SOFTWARE_COMING_SOON
from .shared import section_head, _page_shell


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