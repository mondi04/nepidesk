"""
components/legal.py
Impressum & Datenschutz. Inhalte kommen aus data.py (IMPRESSUM / DATENSCHUTZ),
die ihre Werte wiederum aus config.py / .env beziehen.
"""

from htmforge.elements import div, span, h1, h2, p, a, section

from data import SITE_URL, IMPRESSUM, DATENSCHUTZ
from .shared import _page_shell


def build_impressum_page(css_hash="", js_hash=""):
    imp = IMPRESSUM

    def row(label: str, *children):
        return div(span(label, class_="legal-key"), div(*children, class_="legal-val"), class_="legal-row")

    content = [
        section(
            div(a("← Zurück", href="/", class_="back-link"), class_="subpage-back"),
            h1("Impressum", class_="legal-page-title"),
            p("Angaben gemäß § 5 TMG", class_="legal-subtitle"),

            div(
                h2("Verantwortlicher", class_="legal-section-title"),
                row("Name",       span(imp["name"], class_="legal-text")),
                row("Anschrift",  span(imp["strasse"], class_="legal-text"), span(imp["ort"], class_="legal-text")),
                row("Rechtsform", span(imp["rechtsform"], class_="legal-text")),
                row("E-Mail",     a(imp["email"], href=f"mailto:{imp['email']}", class_="legal-link")),
                class_="legal-block",
            ),

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

            div(
                h2("Streitschlichtung", class_="legal-section-title"),
                p(
                    "Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit: ",
                    a("https://ec.europa.eu/consumers/odr", href="https://ec.europa.eu/consumers/odr",
                      target="_blank", rel="noopener", class_="legal-link"),
                    span(". Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren "
                         "vor einer Verbraucherschlichtungsstelle teilzunehmen."),
                    class_="legal-prose",
                ),
                class_="legal-block",
            ),

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
        "Impressum", "Impressum — NepiDesk", "", content, css_hash, js_hash,
        canonical=SITE_URL + "/impressum",
    )


def build_datenschutz_page(css_hash="", js_hash=""):
    ds = DATENSCHUTZ

    def block(title: str, *paras):
        return div(h2(title, class_="legal-section-title"), *[p(t, class_="legal-prose") for t in paras], class_="legal-block")

    content = [
        section(
            div(a("← Zurück", href="/", class_="back-link"), class_="subpage-back"),
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
                "Die Website wird auf einem eigenen, privat betriebenen Server in Deutschland gehostet. "
                "Es werden keine externen Hosting-Anbieter eingesetzt.",
                "Der Datenverkehr wird über Cloudflare (Cloudflare, Inc., 101 Townsend St., "
                "San Francisco, CA 94107, USA) geleitet. Cloudflare agiert dabei als Reverse-Proxy "
                "und kann dabei technische Metadaten (IP-Adresse, Request-Header) verarbeiten. "
                "Die eigentliche IP-Adresse des Servers wird dabei nicht öffentlich exponiert. "
                "Weitere Informationen: https://www.cloudflare.com/privacypolicy/",
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
                f"Zur Ausübung Ihrer Rechte genügt eine E-Mail an {ds['verantwortlicher_email']}. "
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
        "Datenschutz", "Datenschutzerklärung — NepiDesk", "", content, css_hash, js_hash,
        canonical=SITE_URL + "/datenschutz",
    )