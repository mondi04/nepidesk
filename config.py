"""
config.py — zentrale Konfiguration, lädt Secrets/Settings aus Umgebungsvariablen (.env).

Warum: NepiDesk ist Open Source. Alles was hart im Code steht (SMTP-Zugang,
Grafana-URL, Privatadresse im Impressum) ist für jeden auf GitHub sichtbar.
Das gehört in eine .env, die NICHT committed wird.
"""

import os
from dotenv import load_dotenv

load_dotenv()


def _get(key: str, default: str | None = None, required: bool = False) -> str:
    value = os.environ.get(key, default)
    if required and not value:
        raise RuntimeError(f"Fehlende Umgebungsvariable: {key}. Siehe .env.example.")
    return value


# ── Flask ──────────────────────────────────────────────────
SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-change-in-production")
CONTACT_TO = os.getenv("NEPIDESK_CONTACT_TO")
SMTP_HOST = os.getenv("NEPIDESK_SMTP_HOST")
SMTP_PORT = int(os.getenv("NEPIDESK_SMTP_PORT", "465"))
SMTP_USER = os.getenv("NEPIDESK_SMTP_USER")
SMTP_PASS = os.getenv("NEPIDESK_SMTP_PASS")
RATE_LIMIT_SECONDS = int(os.getenv("RATE_LIMIT_SECONDS", "30"))

# ── Grafana / Infra-Monitoring ────────────────────────────────
GRAFANA_BASE = _get("GRAFANA_BASE", "")

# ── Impressum (Pflichtangabe auf der Seite, aber nicht im Source-Code) ──────
IMPRESSUM_NAME    = _get("IMPRESSUM_NAME", "")
IMPRESSUM_STRASSE = _get("IMPRESSUM_STRASSE", "")
IMPRESSUM_ORT     = _get("IMPRESSUM_ORT", "")
IMPRESSUM_EMAIL   = _get("IMPRESSUM_EMAIL", "kontakt@nepidesk.de")