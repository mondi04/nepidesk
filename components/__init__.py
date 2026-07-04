"""
components/__init__.py
Re-Exports, damit bestehender Code (z. B. app.py) weiterhin
`from components import build_home` etc. nutzen kann.
"""

from .shared import tag_chip, section_head
from .header import build_header
from .footer import build_footer
from .toasts import build_toast_success, build_toast_error, build_toast_sent

from .home import (
    build_home, build_hero, build_ticker,
    build_preview_card, build_home_previews, build_stack,
)
from .kunden import build_kunden_page
from .oss import build_opensource_page
from .software import build_software_page
from .infra import build_infra_page
from .tarife import build_tarife_page
from .kontakt import build_kontakt_form, build_kontakt_success, build_kontakt_page
from .legal import build_impressum_page, build_datenschutz_page

__all__ = [
    "tag_chip", "section_head",
    "build_header", "build_footer",
    "build_toast_success", "build_toast_error", "build_toast_sent",
    "build_home", "build_hero", "build_ticker",
    "build_preview_card", "build_home_previews", "build_stack",
    "build_kunden_page",
    "build_opensource_page",
    "build_software_page",
    "build_infra_page",
    "build_tarife_page",
    "build_kontakt_form", "build_kontakt_success", "build_kontakt_page",
    "build_impressum_page", "build_datenschutz_page",
]