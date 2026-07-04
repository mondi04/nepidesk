"""
components/kontakt.py
"""

from htmforge.elements import (
    div, span, h3, p, a, form, label, input, textarea, select, option, button, section,
)

from data import SITE_URL, KONTAKT_INTRO, KONTAKT_INFO, KONTAKT_BETREFF_OPTIONS
from .shared import section_head, _page_shell


def build_kontakt_form(name: str = "", email: str = "", betreff: str = "",
                        nachricht: str = "", errors: dict | None = None):
    """Rendert (und re-rendert nach Server-Validierung) das Kontaktformular."""
    errors = errors or {}

    def err(field: str):
        return div(errors[field], class_="field-error") if field in errors else span("")

    betreff_opts = [
        option(lbl, value=val, selected=True if val == betreff else None)
        for lbl, val in KONTAKT_BETREFF_OPTIONS
    ]

    return div(
        form(
            div(
                label("Name *", for_="kontakt-name", class_="form-label"),
                input(type="text", name="name", id="kontakt-name", value=name or None,
                      placeholder="Dein Name", required=True, class_="form-input"),
                err("name"),
                class_="form-field",
            ),
            div(
                label("E-Mail *", for_="kontakt-email", class_="form-label"),
                input(type="email", name="email", id="kontakt-email", value=email or None,
                      placeholder="du@example.com", required=True, class_="form-input"),
                err("email"),
                class_="form-field",
            ),
            div(
                label("Betrifft", for_="kontakt-betreff", class_="form-label"),
                select(*betreff_opts, name="betreff", id="kontakt-betreff", class_="form-input"),
                class_="form-field",
            ),
            div(
                label("Nachricht *", for_="kontakt-nachricht", class_="form-label"),
                textarea(nachricht or None, name="nachricht", id="kontakt-nachricht",
                         placeholder="Was möchtest du umsetzen oder wissen?",
                         required=True, rows="6", class_="form-input form-textarea"),
                err("nachricht"),
                class_="form-field",
            ),
            div(
                label("Website", for_="kontakt-website"),
                input(type="text", name="website", id="kontakt-website",
                      tabindex="-1", autocomplete="off"),
                class_="hp-field", aria_hidden="true",
            ),
            button("Nachricht senden", type="submit", class_="form-submit"),
            p(
                "* Pflichtfeld — Angaben werden nur zur Bearbeitung deiner Anfrage genutzt, siehe ",
                a("Datenschutz", href="/datenschutz", class_="accent-link"),
                span("."),
                class_="form-hint",
            ),
            hx_post="/kontakt/senden",
            hx_target="#kontakt-form-wrapper",
            hx_swap="outerHTML",
            class_="contact-form",
        ),
        id="kontakt-form-wrapper",
        class_="contact-form-wrapper reveal",
    )


def build_kontakt_success():
    return div(
        div(
            span("✓", class_="success-icon"),
            h3("Nachricht gesendet", class_="success-title"),
            p(
                "Danke für deine Nachricht — ich melde mich in der Regel innerhalb "
                "von 24 bis 48 Stunden zurück.",
                class_="success-text",
            ),
            a("Neue Nachricht senden", href="/kontakt", class_="svc-btn"),
            class_="success-inner",
        ),
        id="kontakt-form-wrapper",
        class_="contact-success reveal visible",
    )


def build_kontakt_page(css_hash="", js_hash="", betreff=""):
    info_rows = [
        div(
            span(k, class_="info-key"),
            span(v, class_="info-val"),
            class_="info-row reveal",
            data_delay=str(i * 60),
        )
        for i, (k, v) in enumerate(KONTAKT_INFO)
    ]

    content = [
        section(
            section_head("01", "Kontakt", KONTAKT_INTRO),
            div(
                div(
                    div(*info_rows, class_="info-table"),
                    p(
                        "Kein Callcenter, keine Warteschleife — Anfragen landen "
                        "direkt bei mir und werden persönlich beantwortet.",
                        class_="info-prose reveal", data_delay="300",
                    ),
                    class_="kontakt-info",
                ),
                build_kontakt_form(betreff=betreff),
                class_="kontakt-split",
            ),
            class_="section-block",
        ),
    ]
    return _page_shell(
        "Kontakt", "Kontaktiere NepiDesk für Web-Hosting, E-Mail-Hosting oder ein individuelles Projekt.",
        "kontakt", content, css_hash, js_hash,
        canonical=SITE_URL + "/kontakt",
    )