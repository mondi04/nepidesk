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
    {"name": "htmforge",    "role": "HTML-Rendering",    "url": "https://pypi.org/project/htmforge/",             "bar": 100},
    {"name": "Flask",       "role": "Web Framework",     "url": "https://flask.palletsprojects.com/",             "bar": 85},
    {"name": "Gunicorn",    "role": "WSGI Server",       "url": "https://gunicorn.org/",                          "bar": 75},
    {"name": "HTMX",        "role": "Interaktivität",    "url": "https://htmx.org/",                              "bar": 70},
    {"name": "Cloudflare",  "role": "Tunnel & WAF",      "url": "https://cloudflare.com/",                        "bar": 90},
]

HTMFORGE_VERSION = "0.4.0"
SITE_OWNER = "Mondi · NepiDesk"
GRAFANA_URL = "https://monitoring.belchenstrasse5.de?kiosk=tv&viewPanel=0"

GRAFANA_BASE = (
    "https://monitoring.belchenstrasse5.de/d-solo/rYdddlPWk/node-exporter-full"
    "?orgId=1&timezone=browser"
    "&var-ds_prometheus=ef6exteo9p8g0e"
    "&var-job=node&var-nodename=g7"
    "&var-node=192.168.179.10:9100"
    "&refresh=1m"
    "&__feature.dashboardSceneSolo=true"
)

# cols: wie viele Spalten im 3-Spalten-Grid das Panel belegt
GRAFANA_PANELS = [
    {"id": "panel-20",  "label": "CPU Usage",  "cols": 1, "height": 200},
    {"id": "panel-155", "label": "RAM Usage",  "cols": 1, "height": 200},
    {"id": "panel-15",  "label": "Uptime",     "cols": 1, "height": 200},
    {"id": "panel-77",  "label": "CPU Graph",  "cols": 2, "height": 240},
    {"id": "panel-78",  "label": "RAM Graph",  "cols": 1, "height": 240},
]