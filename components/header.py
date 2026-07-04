"""
components/header.py
"Kundenprojekte" steht bewusst an zweiter Stelle direkt nach Start —
das ist das Hauptgeschäft von NepiDesk.
"""

from htmforge.elements import div, span, a, nav, header


def build_header(active: str = "home"):
    nav_links = [
        ("home",        "/",            "Start"),
        ("kunden",      "/kunden",      "Kundenprojekte"),
        ("opensource",  "/opensource",  "Open Source"),
        ("software",    "/software",    "Software"),
        ("infra",       "/infra",       "Infra"),
        ("tarife",      "/tarife",      "Tarife"),
    ]
    nav_items = [
        a(nav_label, href=href, class_=f"nav-link {'nav-active' if key == active else ''}")
        for key, href, nav_label in nav_links
    ]
    return header(
        div(
            a(
                div(
                    span("ND", class_="logo-mark"),
                    div(
                        span("NepiDesk", class_="logo-name"),
                        span("websites · software · security", class_="logo-sub"),
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
                a("Kontakt", href="/kontakt", class_="header-cta"),
                class_="header-right",
            ),
            class_="header-inner",
        ),
        class_="site-header",
    )