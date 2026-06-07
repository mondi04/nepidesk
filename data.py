"""
NepiDesk — nepidesk.de
Alle Inhalte. Keine Logik, keine htmforge-Imports.
"""

HTMFORGE_VERSION = "0.4.0"
SITE_NAME        = "NepiDesk"
SITE_URL         = "https://nepidesk.de"
SITE_AUTHOR      = "Mondi"

# ── Impressum ─────────────────────────────────────────────
IMPRESSUM = {
    "name":          "Moritz Mond",
    "strasse":       "Belchenstrasse 5",
    "ort":           "79677, Aitern",
    "email":         "kontakt@nepidesk.de",
    "rechtsform":    "Privatperson",
    # Sobald du ein Gewerbe anmeldest:
    # "steuernummer": "XX/XXX/XXXXX",
    # "ustid":        "DE XXXXXXXXX",
}

# ── Datenschutz ───────────────────────────────────────────
DATENSCHUTZ = {
    "verantwortlicher_name":  "Moritz Mond",
    "verantwortlicher_email": "kontakt@nepidesk.de",
    "hosting":                "Eigener Server (Self-hosted, Deutschland)",
    "cloudflare":             True,   # Cloudflare Tunnel im Einsatz
}

# ── Hero ──────────────────────────────────────────────────
HERO_CLAIM   = "Software. Security. Open Source."
HERO_SUB     = (
    "Freelance-Entwickler mit Fokus auf Python Web Development, "
    "IT-Security und self-hosted Open-Source-Tools. "
    "Ich baue Dinge, die funktionieren — und zeige wie."
)

# ── Ticker ────────────────────────────────────────────────
TICKER_ITEMS = [
    {"key": "FOCUS",    "value": "Python · Security · Web",    "detail": "Backend-Entwicklung, Pentesting, Open-Source"},
    {"key": "STACK",    "value": "Flask · htmforge · HTMX",    "detail": "Kein Bloat, kein Template-Engine-Overkill"},
    {"key": "HOSTING",  "value": "Self-hosted",                "detail": "Cloudflare Tunnel — kein offener Port, kein Nginx"},
    {"key": "OSS",      "value": "Open Source",                "detail": "htmforge auf PyPI — MIT + Commons Clause"},
    {"key": "SECURITY", "value": "Zero Trust",                 "detail": "WAF, Tunnel, Ed25519 — Security by design"},
]

# ── Home Preview Cards ────────────────────────────────────
# Teaser-Karten auf der Startseite für OSS und Software

HOME_OSS_PREVIEW = {
    "label":   "Open Source",
    "emoji":   "⚒️",
    "tagline": "Python-Bibliotheken, MIT-lizenziert",
    "desc": (
        "Ich entwickle und pflege Open-Source-Bibliotheken, die aus echten "
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
            {"label": "Docs →",   "url": "https://htmforge.nepidesk.de", "primary": True},
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

# ── Grafana ───────────────────────────────────────────────
GRAFANA_BASE = (
    "https://monitoring.belchenstrasse5.de/d-solo/rYdddlPWk/node-exporter-full"
    "?orgId=1&timezone=browser"
    "&var-ds_prometheus=ef6exteo9p8g0e"
    "&var-job=node&var-nodename=g7"
    "&var-node=192.168.179.10:9100"
    "&refresh=1m"
    "&__feature.dashboardSceneSolo=true"
)
GRAFANA_PANELS = [
    {"id": "panel-20",  "label": "CPU Usage", "cols": 1, "height": 200},
    {"id": "panel-155", "label": "RAM Usage", "cols": 1, "height": 200},
    {"id": "panel-15",  "label": "Uptime",    "cols": 1, "height": 200},
    {"id": "panel-77",  "label": "CPU Graph", "cols": 2, "height": 240},
    {"id": "panel-78",  "label": "RAM Graph", "cols": 1, "height": 240},
]

# ── Infra Stack Info ──────────────────────────────────────
INFRA_INFO = [
    ("STACK",   "Prometheus + Node Exporter"),
    ("REFRESH", "1 Minute"),
    ("HOSTING", "Self-hosted · kein Cloud"),
    ("ACCESS",  "Cloudflare Tunnel"),
    ("STATUS",  "Operational ✓"),
]

# ── Unterseiten (SSH, NAS) ────────────────────────────────
SSH_PAGE = {
    "title":   "SSH Terminal",
    "tagline": "Sicherer Web-Zugriff ohne VPN",
    "intro": (
        "Wir nutzen ttyd als Web-Terminal, abgesichert durch Cloudflare WAF, "
        "Rate-Limiting und HTTP Basic Auth. Kein offener SSH-Port, kein VPN — "
        "nur ein Cloudflare Tunnel zwischen Browser und Server."
    ),
    "how": [
        ("Cloudflare Tunnel",   "Verbindet den Server mit Cloudflare — ohne eingehende Firewall-Regel."),
        ("WAF Rate-Limiting",   "Cloudflares WAF blockt Brute-Force automatisch nach 5 Fehlversuchen."),
        ("Basic Auth",          "Einfaches Passwort als erste Verteidigungslinie vor dem Terminal."),
        ("Ed25519 Keys",        "Passwort-Login auf dem Server deaktiviert — nur Key-Auth erlaubt."),
        ("ttyd",                "Leichtgewichtiger Web-Terminal-Server, läuft als systemd-Service."),
    ],
}

NAS_PAGE = {
    "title":   "NAS Storage",
    "tagline": "Redundanter Speicher, kein Cloud-Abo",
    "intro": (
        "Zwei NAS-Geräte (Synology + Buffalo) im lokalen Netz, "
        "synchronisiert per rsync. Medien, Backups, Konfigurationsdaten — "
        "alles lokal, alles unter Kontrolle."
    ),
    "how": [
        ("Synology nas1",    "Primärer NAS — RAID, Medien, aktive Projektdaten."),
        ("Buffalo nas2",     "Backup-NAS — nächtlicher rsync-Sync von nas1."),
        ("rsync via Cron",   "Automatischer Abgleich täglich um 02:00 Uhr."),
        ("Cloudflare Tunnel","Zugriff auf das NAS-UI von überall — ohne Port-Forwarding."),
        ("Netgear GS308E",   "Managed Switch mit VLAN-Isolation für NAS-Traffic."),
    ],
}