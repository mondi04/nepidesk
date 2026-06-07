"""
NepiDesk — nepidesk.de
Alle Inhalte. Keine Logik, keine htmforge-Imports.
"""

HTMFORGE_VERSION = "0.4.0"
SITE_NAME        = "NepiDesk"
SITE_URL         = "https://nepidesk.de"
SITE_AUTHOR      = "Moritz"

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

# ── Projekte / Tools ──────────────────────────────────────
PROJECTS = [
    {
        "id":      "htmforge",
        "emoji":   "⚒️",
        "label":   "htmforge",
        "tagline": "HTML ohne Templates",
        "desc":    (
            "Open-Source Python-Bibliothek für typsicheres HTML-Rendering. "
            "Kein Jinja, kein Template-Ordner — alles in Python. "
            f"Diese Seite ist live damit gebaut."
        ),
        "url":     f"https://htmforge.nepidesk.de",
        "cta":     "Mehr erfahren →",
        "tag":     "oss",
        "external": False,
    },
    {
        "id":      "gitea",
        "emoji":   "📦",
        "label":   "Gitea",
        "tagline": "Self-hosted Git",
        "desc":    (
            "Eigene Git-Instanz — alle Repos, CI/CD-Pipelines und Releases "
            "laufen lokal. Kein GitHub-Abo, keine Abhängigkeit von Dritten."
        ),
        "url":     "https://git.nepidesk.de",
        "cta":     "Öffnen →",
        "tag":     "dev",
        "external": True,
    },
    {
        "id":      "ssh",
        "emoji":   "⌨️",
        "label":   "SSH Terminal",
        "tagline": "Internes Tool",
        "desc":    (
            "Web-Terminal via ttyd, gesichert durch Cloudflare WAF und "
            "Basic Auth. Zeigt wie wir sicheren Remote-Zugriff ohne "
            "VPN und ohne offene Ports realisieren."
        ),
        "url":     "/ssh",
        "cta":     "Wie wir es nutzen →",
        "tag":     "sys",
        "external": False,
    },
    {
        "id":      "nas",
        "emoji":   "💾",
        "label":   "NAS Storage",
        "tagline": "Internes Tool",
        "desc":    (
            "Redundanter Netzwerkspeicher mit automatischem Backup-Sync. "
            "Zwei Geräte, ein Workflow — zeigt unseren Ansatz für "
            "zuverlässige Datenhaltung ohne Cloud."
        ),
        "url":     "/nas",
        "cta":     "Wie wir es nutzen →",
        "tag":     "sys",
        "external": False,
    },
]

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

# ── Unterseiten ───────────────────────────────────────────
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