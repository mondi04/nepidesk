"""
components/tarife.py
Zeigt die zwei Vertragsmodelle (Sorglos/Flex), gemeinsame Grundleistungen,
Stundenkontingente und den E-Mail-Zusatz.
"""

from htmforge.elements import div, span, h2, h3, p, ul, li, a, section

from data import (
    SITE_URL, TARIFE_INTRO, TARIFE_GRUNDLEISTUNGEN, VERTRAGSMODELLE,
    STUNDENKONTINGENTE, STUNDENKONTINGENT_HINWEIS, EMAIL_ADDON, TARIFE_FAQ,
)
from .shared import section_head, _page_shell


def _vertrag_card(plan: dict, index: int):
    feature_items = [
        li(span("✓", class_="feature-check"), span(f, class_="feature-text"), class_="feature-item")
        for f in plan["features"]
    ]
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
    )


def _kontingent_block():
    rows = [
        div(
            span(k["name"], class_="meta-key"),
            span(k["stunden"], class_="meta-val"),
            span(f"{k['preis']}€/Monat", class_="price-amount"),
            class_="meta-row",
        )
        for k in STUNDENKONTINGENTE
    ]
    return div(
        h2("Stundenkontingent (nur bei Sorglos)", class_="tarife-group-title"),
        div(*rows, class_="oss-meta"),
        p(STUNDENKONTINGENT_HINWEIS, class_="info-prose reveal"),
        class_="tarife-group-head reveal",
    )


def _email_addon_block():
    addon = EMAIL_ADDON
    return div(
        h2(addon["name"], class_="tarife-group-title"),
        div(
            span(f"{addon['grundgebuehr']}€", class_="price-amount"),
            span("/ Monat", class_="price-period"),
            class_="price-line",
        ),
        p(addon["desc"], class_="price-desc"),
        p(
            f"Inklusive: {addon['inklusive_postfaecher']} Postfächer à "
            f"{addon['inklusive_groesse']} · jedes weitere Postfach "
            f"{addon['weiteres_postfach']}€/Monat.",
            class_="info-prose reveal",
        ),
        class_="tarife-group-head reveal",
    )


def build_tarife_page(css_hash="", js_hash=""):
    vertrag_cards = [_vertrag_card(p, i) for i, p in enumerate(VERTRAGSMODELLE)]

    faq_rows = [
        div(
            span(q, class_="how-key"),
            p(a_txt, class_="how-val"),
            class_="how-row reveal",
            data_delay=str(i * 60),
        )
        for i, (q, a_txt) in enumerate(TARIFE_FAQ)
    ]

    content = [
        section(
            section_head("01", "Tarife", TARIFE_INTRO),
            div(*vertrag_cards, class_="pricing-grid"),
            class_="section-block",
        ),
        section(
            _grundleistungen_block(),
            class_="section-block",
        ),
        section(
            _kontingent_block(),
            class_="section-block",
        ),
        section(
            _email_addon_block(),
            class_="section-block",
        ),
        section(
            section_head("02", "Häufige Fragen", "Kurz erklärt, warum wir Dinge so machen wie wir sie machen."),
            div(*faq_rows, class_="how-grid"),
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