"""
components/footer.py
"""

from htmforge.elements import footer, div, span, a
from data import SITE_AUTHOR, HTMFORGE_VERSION


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