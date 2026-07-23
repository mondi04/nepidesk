"""
NepiDesk — nepidesk.de
Alle Inhalte. Keine Logik, keine htmforge-Imports.
"""

from config import IMPRESSUM_NAME, IMPRESSUM_STRASSE, IMPRESSUM_ORT, IMPRESSUM_EMAIL

HTMFORGE_VERSION = "0.5.1"
SITE_NAME        = "NepiDesk"
SITE_URL         = "https://nepidesk.de"
SITE_AUTHOR      = "Mondi"

# ── Impressum ─────────────────────────────────────────────
# Werte kommen aus config.py / .env — Privatadresse gehört nicht in den
# öffentlichen Source-Code.
IMPRESSUM = {
    "name":       IMPRESSUM_NAME,
    "strasse":    IMPRESSUM_STRASSE,
    "ort":        IMPRESSUM_ORT,
    "email":      IMPRESSUM_EMAIL,
    "rechtsform": "Privatperson",
    # Sobald du ein Gewerbe anmeldest:
    # "steuernummer": "XX/XXX/XXXXX",
    # "ustid":        "DE XXXXXXXXX",
}

# ── Datenschutz ───────────────────────────────────────────
DATENSCHUTZ = {
    "verantwortlicher_name":  IMPRESSUM_NAME,
    "verantwortlicher_email": IMPRESSUM_EMAIL,
    "hosting":                "Eigener Server (Self-hosted, Deutschland)",
    "cloudflare":             True,
}

# ── Hero ──────────────────────────────────────────────────
# Hauptgeschäft: Websites für Kunden. Steht jetzt zuerst, nicht mehr am Ende.
HERO_CLAIM = "Individuelle Websites für Kunden."
HERO_SUB = (
    "Freelance-Entwickler mit Fokus auf Python Web Development — "
    "Websites für Vereine, Selbstständige und kleine Unternehmen. "
    "Dazu Open-Source-Tools und self-hosted Infrastruktur, "
    "aus derselben Werkstatt."
)

# ── Ticker ────────────────────────────────────────────────
TICKER_ITEMS = [
    {"key": "FOCUS",    "value": "Websites für Kunden",         "detail": "Vereine, Selbstständige, kleine Unternehmen"},
    {"key": "STACK",    "value": "Flask · htmforge · HTMX",     "detail": "Kein Bloat, kein Template-Engine-Overkill"},
    {"key": "HOSTING",  "value": "Self-hosted",                 "detail": "Cloudflare Tunnel — kein offener Port, kein Nginx"},
    {"key": "OSS",      "value": "Open Source",                 "detail": "htmforge auf PyPI — MIT + Commons Clause"},
    {"key": "SECURITY", "value": "Zero Trust",                  "detail": "WAF, Tunnel, Ed25519 — Security by design"},
]

# ── Kundenprojekte (Hauptgeschäft) ────────────────────────
KUNDEN_INTRO = (
    "Individuelle Websites für Vereine, Selbstständige und kleine Unternehmen — "
    "kein Baukasten, kein WordPress-Plugin-Chaos, sondern handgeschriebener, "
    "schneller Code, der zu 100 % zum Kunden passt."
)

KUNDEN_PROJECTS = [
    {
        "emoji": "🏕️",
        "label": "Vereinslösungen",
        "tagline": "Verein · Wiki & Mitgliederportal · Fotogalerie",
        "desc": (
            "Self-hosted Wiki- und Informationssystem für einen Verein, "
            "inkl. individuellem Design-System und News-/Rezepte-Feeds."
        ),
        "meta": [("Typ", "Verein"), ("Stack", "Wiki.js · GraphQL · JS")],
        "url": "",  # TODO: echte URL eintragen, falls öffentlich verlinkbar
    },
    {
        "emoji": "🛠️",
        "label": "Handwerksbetrieb",
        "tagline": "Kleines Unternehmen · Portfolio & Kontakt",
        "desc": (
            "Individuelle Website für einen Handwerksbetrieb, "
            "inkl. Portfolio, Kontaktformular und DSGVO-konformer Umsetzung."
        ),
        "meta": [("Typ", "Kleines Unternehmen"), ("Stack", "Flask · htmforge · HTMX")],
        "url": "",  # TODO: echte URL eintragen, falls öffentlich verlinkbar
    },
    {
        "emoji": "🎨",
        "label": "Kreativagentur",
        "tagline": "Selbstständige · Portfolio & Blog",
        "desc": (
            "Website für eine Kreativagentur, mit Portfolio, Blog und "
            "individuellem Design-System."
        ),
        "meta": [("Typ", "Selbstständige"), ("Stack", "Flask · htmforge · HTMX")],
        "url": "",  # TODO: echte URL eintragen, falls öffentlich verlinkbar
    },
    {
        "emoji": "💼",
        "label": "Beratungsfirma",
        "tagline": "Kleines Unternehmen · Portfolio & Kontakt",
        "desc": (
            "Individuelle Website für eine Beratungsfirma, "
            "inkl. Portfolio, Kontaktformular und DSGVO-konformer Umsetzung."
        ),
        "meta": [("Typ", "Kleines Unternehmen"), ("Stack", "Flask · htmforge · HTMX")],
        "url": "",  # TODO: echte URL eintragen, falls öffentlich verlinkbar
    }
]

# ── Home Preview Cards ────────────────────────────────────
HOME_KUNDEN_PREVIEW = {
    "label":   "Kundenprojekte",
    "emoji":   "🌐",
    "tagline": "Individuelle Websites",
    "desc": (
        "Vereine, Selbstständige, kleine Unternehmen — von der Idee bis zum "
        "Go-Live, inklusive Hosting und Betreuung danach."
    ),
    "count":   f"{len(KUNDEN_PROJECTS)} Projekte",
    "url":     "/kunden",
    "cta":     "Ansehen →",
    "tag":     "kunde",
}

HOME_TARIFE_PREVIEW = {
    "label":   "Tarife",
    "emoji":   "💶",
    "tagline": "Sorglos oder Flex — transparente Preise",
    "desc": (
        "Zwei fertige Vertragsmodelle für Website-Hosting, klar kalkuliert. "
        "Kein Kleingedrucktes, keine versteckten Kosten."
    ),
    "count":   "Ab 7,99€ / Monat",
    "url":     "/tarife",
    "cta":     "Preise ansehen →",
    "tag":     "dev",
}

HOME_EMAIL_PREVIEW = {
    "label":   "E-Mail Hosting (Optional zur Website)",
    "emoji":   "📧",
    "tagline": "Professionelle E-Mail auf eigener Domain",
    "desc": (
        "3 Postfächer inklusive, optional erweiterbar. "
        "Inklusive Spam-Filter, TLS-Verschlüsselung und DSGVO-konformem Hosting."
    ),
    "count":   "5€/Monat",
    "url":     "/tarife#email-addon",
    "cta":     "E-Mail ansehen →",
    "tag":     "email",
}

HOME_OSS_PREVIEW = {
    "label":   "Open Source",
    "emoji":   "⚒️",
    "tagline": "Python-Bibliotheken, MIT-lizenziert",
    "desc": (
        "Wir entwickeln und pflegen Open-Source-Bibliotheken, die aus echten "
        "Projekten entstehen — kein Spielzeug, sondern produktiv eingesetzter Code. "
        "Aktuell zwei Pakete auf PyPI."
    ),
    "count":   "2 Pakete auf PyPI",
    "url":     "/opensource",
    "cta":     "Alle Projekte →",
    "tag":     "oss",
}

HOME_SOFTWARE_PREVIEW = {
    "label":   "Software",
    "emoji":   "🖥️",
    "tagline": "Desktop & Web Applikationen",
    "desc": (
        "Kommerzielle und interne Software — Desktop-Apps mit Avalonia, "
        "Web-Apps mit Flask. Für Kunden und für den eigenen Betrieb."
    ),
    "count":   "Coming soon",
    "url":     "/software",
    "cta":     "Mehr erfahren →",
    "tag":     "dev",
}

HOME_INFRA_PREVIEW = {
    "label":   "Infra",
    "emoji":   "🖧",
    "tagline": "Self-hosted · Zero Trust · Kein Cloud-Zwang",
    "desc": (
        "Eigene Server, Cloudflare Tunnel, Grafana-Monitoring — "
        "alles unter Kontrolle. Live-Metriken und Einblick in den Stack."
    ),
    "count":   "Live Monitoring",
    "url":     "/infra",
    "cta":     "Infra ansehen →",
    "tag":     "sys",
}

# ── OSS Projekte ──────────────────────────────────────────
OSS_PROJECTS = [
    {
        "id":       "htmforge",
        "emoji":    "⚒️",
        "label":    "htmforge",
        "tagline":  "HTML ohne Templates",
        "desc": (
            "Open-Source Python-Bibliothek für typsicheres HTML-Rendering. "
            "Kein Jinja, kein Template-Ordner — alles in Python. "
            "Pydantic-validiert, markupsafe-escaped, produktionsreif. "
            "Diese Seite ist live damit gebaut."
        ),
        "meta": [
            ("PyPI",     "htmforge"),
            ("Lizenz",   "MIT + Commons Clause"),
            ("Version",  f"v{HTMFORGE_VERSION}"),
            ("Status",   "Aktiv"),
        ],
        "links": [
            {"label": "Docs →",   "url": "https://mondi04.github.io/htmforge/", "primary": True},
            {"label": "Beispiel ↗", "url": "https://htmforge.nepidesk.de", "primary": True},
            {"label": "PyPI ↗",   "url": "https://pypi.org/project/htmforge/", "primary": False},
        ],
        "tag": "oss",
    },
    {
        "id":       "edgesync",
        "emoji":    "📡",
        "label":    "edgesync",
        "tagline":  "MQTT Config Sync für Edge Devices",
        "desc": (
            "Leichtgewichtiges Python-Tool zur Konfigurationssynchronisation "
            "von Edge-Device-Flotten über MQTT. Pydantic v2 Modelle, "
            "Hook-System, Agent/Fleet-Klassen — minimal, robust, testbar."
        ),
        "meta": [
            ("PyPI",     "edgesync"),
            ("Lizenz",   "MIT"),
            ("Version",  "v0.1.0"),
            ("Status",   "Beta"),
        ],
        "links": [
            {"label": "PyPI ↗",    "url": "https://pypi.org/project/edgesync/", "primary": True},
            {"label": "GitHub ↗",  "url": "https://github.com/mondi04/edgesync", "primary": False},
        ],
        "tag": "oss",
    },
]

# ── Software Platzhalter ──────────────────────────────────
SOFTWARE_COMING_SOON = {
    "title":   "Software Projekte",
    "tagline": "Desktop & Web — Coming Soon",
    "intro": (
        "Hier werden demnächst kommerzielle und interne Software-Projekte vorgestellt: "
        "Desktop-Applikationen mit Avalonia UI, Web-Apps mit Flask und Python, "
        "sowie interne Tools für den Geschäftsbetrieb."
    ),
    "teaser": [
        {
            "emoji": "🖥️",
            "label": "Desktop Apps",
            "desc":  "Avalonia UI · EF Core · CommunityToolkit.Mvvm — plattformübergreifende Desktop-Anwendungen.",
            "status": "in Entwicklung",
        },
        {
            "emoji": "🌐",
            "label": "Web Apps",
            "desc":  "Flask · htmforge · HTMX — schlanke Web-Applikationen ohne Framework-Overhead.",
            "status": "in Entwicklung",
        },
        {
            "emoji": "🔧",
            "label": "Interne Tools",
            "desc":  "Maßgeschneiderte Lösungen für Workflows, Automatisierung und Datenverwaltung.",
            "status": "in Entwicklung",
        },
    ],
}

# ── Stack ─────────────────────────────────────────────────
STACK = [
    {"name": "htmforge",   "role": "HTML-Rendering — kein Template",  "url": "https://pypi.org/project/htmforge/",   "bar": 100},
    {"name": "Python",     "role": "Primäre Sprache",                 "url": "https://python.org/",                  "bar": 95},
    {"name": "Flask",      "role": "Web Framework",                   "url": "https://flask.palletsprojects.com/",   "bar": 88},
    {"name": "HTMX",       "role": "Frontend-Interaktivität",         "url": "https://htmx.org/",                    "bar": 75},
    {"name": "Cloudflare", "role": "Tunnel, WAF, Zero Trust",         "url": "https://cloudflare.com/",              "bar": 90},
    {"name": "Gunicorn",   "role": "WSGI Production Server",          "url": "https://gunicorn.org/",                "bar": 70},
]

# ── Infra Stack Info ──────────────────────────────────────
# GRAFANA_BASE kommt jetzt NICHT mehr aus data.py, sondern direkt aus
# config.py in components/infra.py — steht deshalb hier absichtlich nicht mehr.
GRAFANA_PANELS = [
    {"id": "panel-20",  "label": "CPU Usage", "cols": 1, "height": 200},
    {"id": "panel-155", "label": "RAM Usage", "cols": 1, "height": 200},
    {"id": "panel-15",  "label": "Uptime",    "cols": 1, "height": 200},
    {"id": "panel-77",  "label": "CPU Graph", "cols": 2, "height": 240},
    {"id": "panel-78",  "label": "RAM Graph", "cols": 1, "height": 240},
]

INFRA_INFO = [
    ("STACK",   "Prometheus + Node Exporter"),
    ("REFRESH", "1 Minute"),
    ("HOSTING", "Self-hosted · kein Cloud"),
    ("ACCESS",  "Cloudflare Tunnel"),
    ("STATUS",  "Operational ✓"),
]

# ── Tarife ────────────────────────────────────────────────
# Entspricht §2/§3 der Verträge "Sorglos" und "Flex".

TARIFE_INTRO = (
    "Zwei Vertragsmodelle, klar kalkuliert. Hosting, Domain, SSL und DB-Backups "
    "sind in beiden Modellen identisch — der Unterschied liegt darin, wie "
    "Änderungen an deiner Website abgerechnet werden."
)

# Leistungen, die in BEIDEN Vertragsmodellen identisch enthalten sind (§2)
TARIFE_GRUNDLEISTUNGEN = [
    ("Website-Technologie", "Python-basierte Webanwendung (Flask/htmforge)"),
    ("SSL-Zertifikat",      "Inklusive via Cloudflare, Datenweitergabe in AVV geregelt"),
    ("DB-Backups",             "Täglich, 7 Tage Aufbewahrung"),
    ("Uptime-Ziel",         "99 % pro Kalendermonat"),
    ("Domain (INWX.de)",    "Wird von uns registriert und verwaltet — verbleibt nach Vertragsende beim Auftraggeber"),
]

VERTRAGSMODELLE = [
    {
        "id":        "sorglos",
        "name":      "Sorglos",
        "tagline":   "Planbare Kosten, festes Stundenkontingent",
        "einrichtung": 300,
        "hosting":   7.99,
        "highlight": True,
        "badge":     "Empfehlung",
        "desc": (
            "Du wählst ein monatliches Anpassungskontingent (siehe unten) und "
            "zahlst dafür einen festen Betrag. Änderungen darüber hinaus werden "
            "mit 35 €/Std. abgerechnet (10-Minuten-Taktung)."
        ),
        "features": [
            "Einmalige Einrichtung: 300 €",
            "Hosting-Gebühr: 7,99 €/Monat (Server + Domain)",
            "Inkludierte Anpassungsstunden gemäß gewähltem Stundenkontingent",
            "Änderungsstundensatz zusätzlich: 35 €/Std. (10-Min-Taktung)",
            "E-Mail optional: ab 5 €/Monat",
        ],
        "cta_label": "Sorglos anfragen",
    },
    {
        "id":        "flex",
        "name":      "Flex",
        "tagline":   "Nur zahlen, was wirklich gebraucht wird",
        "einrichtung": 500,
        "hosting":   7.99,
        "highlight": False,
        "badge":     "",
        "desc": (
            "Keine festen Anpassungsstunden — du zahlst nur die Hosting-Gebühr. "
            "Jede Änderung wird nach Aufwand mit 45 €/Std. abgerechnet "
            "(10-Minuten-Taktung)."
        ),
        "features": [
            "Einmalige Einrichtung: 500 €",
            "Hosting-Gebühr: 7,99 €/Monat (Server + Domain)",
            "Keine inkludierten Anpassungsstunden",
            "Änderungsstundensatz: 45 €/Std. (10-Min-Taktung)",
            "E-Mail optional: ab 5 €/Monat",
        ],
        "cta_label": "Flex anfragen",
    },
]

STUNDENKONTINGENTE = [
    {"name": "Basis",     "stunden": "1 Stunde Anpassung / Monat",      "preis": 20},
    {"name": "Komfort",   "stunden": "2 Stunden Anpassung / Monat",     "preis": 35},
    {"name": "Erweitert", "stunden": "3 Stunden Anpassung / Monat",     "preis": 45},
    {"name": "Premium",   "stunden": "4 Stunden Anpassung / Monat",     "preis": 53},
    {"name": "Intensiv",  "stunden": "bis zu 5 Std. Anpassung / Monat", "preis": 60},
]

STUNDENKONTINGENT_HINWEIS = (
    "Nicht in Anspruch genommene Stunden verfallen am Ende des jeweiligen "
    "Kalendermonats und werden nicht übertragen. Zusätzliche Stunden über das "
    "gewählte Kontingent hinaus werden gemäß Änderungsstundensatz (35 €/Std.) "
    "abgerechnet."
)

EMAIL_ADDON = {
    "name":                  "E-Mail (Migadu)",
    "grundgebuehr":          5,
    "inklusive_postfaecher": 3,
    "inklusive_groesse":     "1 GB",
    "weiteres_postfach":     2,
    "desc": (
        "3 professionelle E-Mail-Postfächer auf deiner eigenen Domain, je 1 GB "
        "Speicher, inklusive. "
        "Jedes weitere Postfach kostet 2 €/Monat zusätzlich. "
        "Nach weiterer Absprache können auch größere Postfächer oder zusätzliche Features (z. B. "
        "automatische Backups) hinzugefügt werden."
    ),
}

TARIFE_FAQ = [
    ("Sorglos oder Flex — was passt zu mir?",
     "Wer regelmäßig kleine Anpassungen braucht, fährt mit Sorglos meist günstiger. "
     "Wer nach dem Launch kaum noch Änderungen braucht, spart mit Flex."),
    ("Was zählt als 'Änderung'?",
     "Jede inhaltliche oder technische Anpassung an der bestehenden Website — "
     "abgerechnet in 10-Minuten-Schritten, damit auch kleine Anfragen fair "
     "berechnet werden."),
    ("Kann ich später zwischen Sorglos und Flex wechseln?",
     "Ja, ein Wechsel ist zum nächsten Abrechnungsmonat jederzeit möglich."),
    ("Ist die Domain danach meine?",
     "Ja — die Domain wird zwar von uns über INWX registriert und verwaltet, "
     "verbleibt nach Vertragsende aber beim Auftraggeber."),
]

# ── Kontakt ───────────────────────────────────────────────
KONTAKT_INTRO = (
    "Fragen zu einem Vertragsmodell, ein individuelles Projekt oder einfach "
    "Interesse? Schreib mir — ich melde mich in der Regel innerhalb von 24 bis "
    "48 Stunden zurück."
)

KONTAKT_INFO = [
    ("E-MAIL",     "kontakt@nepidesk.de"),
    ("REAKTION",   "24–48 Stunden"),
    ("STANDORT",   "Schwarzwald, Deutschland"),
    ("SPRACHEN",   "Deutsch · Englisch"),
]

KONTAKT_BETREFF_OPTIONS = [
    ("Vertrag Sorglos",       "sorglos"),
    ("Vertrag Flex",          "flex"),
    ("E-Mail-Hosting",        "email-hosting"),
    ("Individuelles Projekt", "individuell"),
    ("Sonstiges",             "sonstiges"),
]