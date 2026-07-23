"""
components/tarife.py
Zeigt die zwei Vertragsmodelle (Sorglos/Flex), gemeinsame Grundleistungen,
Stundenkontingente und den E-Mail-Zusatz.
"""

from htmforge.elements import (
    div, span, h2, h3, p, ul, li, a, section,
    table, thead, tbody, tr, th, td, details, summary,
)

from data import (
    SITE_URL, TARIFE_INTRO, TARIFE_GRUNDLEISTUNGEN, VERTRAGSMODELLE,
    STUNDENKONTINGENTE, STUNDENKONTINGENT_HINWEIS, EMAIL_ADDON, TARIFE_FAQ,
)
from .shared import section_head, _page_shell


def _fmt_eur(value):
    return f"{value}".replace(".", ",") + "€"


def _trust_bar():
    items = [
        ("🛡️", "99 % Uptime-Ziel"),
        ("💾", "Tägliche Backups · 7 Tage"),
        ("🔑", "Domain bleibt bei dir"),
        ("🔒", "SSL inklusive"),
    ]
    chips = [
        div(span(icon, class_="trust-icon"), span(label), class_="trust-item")
        for icon, label in items
    ]
    return div(*chips, class_="trust-bar reveal")


def _compare_table():
    sorglos, flex = VERTRAGSMODELLE[0], VERTRAGSMODELLE[1]
    aenderung = {
        "sorglos": "Kontingent inklusive, danach 30 €/Std.",
        "flex":    "Keine Inklusivstunden, 50 €/Std.",
    }
    passt_zu = {
        "sorglos": "Regelmäßige, kleine Anpassungen",
        "flex":    "Selten benötigte Änderungen",
    }
    rows = [
        ("Einrichtung", _fmt_eur(sorglos["einrichtung"]) + " einmalig", _fmt_eur(flex["einrichtung"]) + " einmalig"),
        ("Hosting",     _fmt_eur(sorglos["hosting"]) + " / Monat",      _fmt_eur(flex["hosting"]) + " / Monat"),
        ("Änderungen",  aenderung["sorglos"],                          aenderung["flex"]),
        ("Passt zu",    passt_zu["sorglos"],                           passt_zu["flex"]),
    ]
    body_rows = [
        tr(
            td(label, class_="compare-row-label"),
            td(v1, class_="compare-highlight"),
            td(v2),
        )
        for label, v1, v2 in rows
    ]
    return div(
        table(
            thead(
                tr(
                    th(""),
                    th(sorglos["name"], class_="compare-th-featured"),
                    th(flex["name"]),
                )
            ),
            tbody(*body_rows),
            class_="compare-table",
        ),
        class_="compare-wrap reveal",
    )


def _vertrag_card(plan: dict, index: int):
    feature_items = [
        li(span("✓", class_="feature-check"), span(f, class_="feature-text"), class_="feature-item")
        for f in plan["features"]
    ]
    kontingent_block = span("")
    if plan["id"] == "sorglos":
        rows = [
            div(
                span(k["name"], class_="price-kontingent-name"),
                span(k["stunden"], class_="price-kontingent-hours"),
                span(f"{k['preis']}€/Mon.", class_="price-kontingent-price"),
                class_="price-kontingent-row",
            )
            for k in STUNDENKONTINGENTE
        ]
        kontingent_block = div(
            span("Stundenkontingent wählen", class_="price-kontingent-label"),
            *rows,
            p(STUNDENKONTINGENT_HINWEIS, class_="price-kontingent-hint"),
            class_="price-kontingent",
        )
    return div(
        span(plan["badge"], class_="price-badge") if plan["badge"] else span(""),
        h3(plan["name"], class_="price-name"),
        p(plan["tagline"], class_="price-tagline"),
        div(
            span(f"{plan['hosting']}€".replace(".", ","), class_="price-amount"),
            span("/ Monat", class_="price-period"),
            class_="price-line",
        ),
        p(f"+ {plan['einrichtung']}€ einmalige Einrichtung", class_="price-note"),
        p(plan["desc"], class_="price-desc"),
        ul(*feature_items, class_="price-features"),
        kontingent_block,
        a(plan["cta_label"], href=f"/kontakt?betreff={plan['id']}", class_="price-cta"),
        class_=f"price-card reveal {'price-card-featured' if plan['highlight'] else ''}",
        data_delay=str(index * 100),
    )


def _grundleistungen_block():
    rows = [
        div(
            span(k, class_="how-key"),
            p(v, class_="how-val"),
            class_="how-row reveal", data_delay=str(i * 60),
        )
        for i, (k, v) in enumerate(TARIFE_GRUNDLEISTUNGEN)
    ]
    return div(
        h2("In beiden Modellen enthalten", class_="tarife-group-title"),
        div(*rows, class_="how-grid"),
        class_="tarife-group-head reveal",
        id="email-addon",
    )


def _email_addon_block():
    addon = EMAIL_ADDON
    return div(
        div(
            h2(addon["name"], class_="tarife-group-title"),
            p(addon["desc"], class_="price-desc"),
            p(
                f"Inklusive: {addon['inklusive_postfaecher']} Postfächer à "
                f"{addon['inklusive_groesse']} · jedes weitere Postfach "
                f"{addon['weiteres_postfach']}€/Monat.",
                class_="info-prose",
            ),
            class_="offer-main",
        ),
        div(
            span(f"{addon['grundgebuehr']}€", class_="price-amount"),
            span("/ Monat", class_="price-period"),
            class_="price-line",
        ),
        class_="offer-card reveal",
    )


def _faq_accordion():
    items = [
        details(
            summary(q),
            p(a_txt, class_="faq-body"),
            class_="faq-item reveal",
            data_delay=str(i * 60),
        )
        for i, (q, a_txt) in enumerate(TARIFE_FAQ)
    ]
    return div(*items, class_="faq-accordion")


def build_tarife_page(css_hash="", js_hash=""):
    vertrag_cards = [_vertrag_card(p, i) for i, p in enumerate(VERTRAGSMODELLE)]

    content = [
        section(
            section_head("01", "Tarife", TARIFE_INTRO),
            _trust_bar(),
            _compare_table(),
            div(*vertrag_cards, class_="pricing-grid"),
            class_="section-block",
        ),
        section(
            _grundleistungen_block(),
            class_="section-block",
        ),
        section(
            _email_addon_block(),
            class_="section-block",
        ),
        section(
            section_head("02", "Häufige Fragen", "Kurz erklärt, warum wir Dinge so machen wie wir sie machen."),
            _faq_accordion(),
            class_="section-block",
        ),
        section(
            div(
                h2("Unsicher, welches Modell passt?", class_="cta-banner-title"),
                p(
                    "Schreib mir kurz was du vorhast — wir finden gemeinsam heraus, "
                    "ob Sorglos oder Flex besser zu deinem Projekt passt.",
                    class_="cta-banner-sub",
                ),
                a("Kontakt aufnehmen", href="/kontakt", class_="cta-primary"),
                class_="cta-banner reveal",
            ),
            class_="section-block",
        ),
    ]
    return _page_shell(
        "Tarife", "Sorglos oder Flex — transparente Preise für Website-Hosting bei NepiDesk.",
        "tarife", content, css_hash, js_hash,
        canonical=SITE_URL + "/tarife",
    )