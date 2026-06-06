"""
Alle Inhalte der Seite — keine Logik, keine Imports aus htmforge.
"""

SERVICES = [
    {
        "id": "gitea",
        "emoji": "📦",
        "label": "Gitea",
        "desc": "Self-hosted Git. Alle Repos, CI/CD-Pipelines, Releases — lokal, kein GitHub erforderlich.",
        "url": "https://git.belchenstrasse5.de",
        "tag": "dev",
        "status": "online",
    },
    {
        "id": "plane",
        "emoji": "✈️",
        "label": "Plane",
        "desc": "Projektmanagement. Issues, Sprints, Roadmaps — für alle laufenden NepiDesk-Projekte.",
        "url": "https://plan.belchenstrasse5.de",
        "tag": "mgmt",
        "status": "online",
    },
    {
        "id": "ssh",
        "emoji": "⌨️",
        "label": "SSH Terminal",
        "desc": "Web-Terminal via ttyd + Cloudflare WAF. Direktzugriff auf g7 vom Browser.",
        "url": "https://ssh.belchenstrasse5.de",
        "tag": "sys",
        "status": "online",
    },
    {
        "id": "nas",
        "emoji": "💾",
        "label": "NAS Storage",
        "desc": "Synology nas1 + Buffalo nas2. Redundanter Speicher, automatischer Backup-Sync.",
        "url": "https://nas.belchenstrasse5.de",
        "tag": "sys",
        "status": "online",
    },
]

SERVER_SPECS = [
    {
        "key": "HOST",
        "value": "g7",
        "detail": "Ubuntu 22.04 LTS — 16 GB DDR3 — 24/7",
    },
    {
        "key": "NET",
        "value": "Cloudflare Tunnel",
        "detail": "*.belchenstrasse5.de → localhost — kein offener Port",
    },
    {
        "key": "ROUTER",
        "value": "MikroTik",
        "detail": "Managed Routing, VLANs, Netgear GS308E Switch",
    },
    {
        "key": "STORAGE",
        "value": "2× NAS",
        "detail": "Synology + Buffalo — RAID, Medien, Config-Backups",
    },
    {
        "key": "MONITOR",
        "value": "Grafana",
        "detail": "Prometheus + Node Exporter — Live-Metriken",
    },
]

STACK = [
    {"name": "htmforge",    "role": "HTML-Rendering",    "url": "https://pypi.org/project/htmforge/"},
    {"name": "Flask",       "role": "Web Framework",     "url": "https://flask.palletsprojects.com/"},
    {"name": "Gunicorn",    "role": "WSGI Server",       "url": "https://gunicorn.org/"},
    {"name": "HTMX",        "role": "Interaktivität",    "url": "https://htmx.org/"},
    {"name": "Cloudflare",  "role": "Tunnel & WAF",      "url": "https://cloudflare.com/"},
]

HTMFORGE_VERSION = "0.4.0"
SITE_OWNER = "Mondi · NepiDesk"
GRAFANA_URL = "https://monitoring.belchenstrasse5.de?kiosk=tv&viewPanel=0"