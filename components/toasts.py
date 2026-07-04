"""
components/toasts.py
"""

from htmforge.components.toast import Toast, ToastVariant


def build_toast_success():
    return Toast(message="✓ URL kopiert", variant=ToastVariant.SUCCESS, duration_ms=2500)


def build_toast_error(message: str):
    return Toast(message=f"⚠ {message}", variant=ToastVariant.ERROR, duration_ms=4500)


def build_toast_sent(message: str = "Nachricht gesendet"):
    return Toast(message=f"✓ {message}", variant=ToastVariant.SUCCESS, duration_ms=3000)