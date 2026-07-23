# app.py - komplett neu für Kontakt

import hashlib
import re
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta
from flask import Flask, Response, request, send_from_directory
from components import (
    build_home,
    build_toast_success,
    build_kunden_page,
    build_opensource_page,
    build_software_page,
    build_infra_page,
    build_impressum_page,
    build_datenschutz_page,
    build_tarife_page,
    build_kontakt_page,
    build_kontakt_form,
    build_kontakt_success,
    build_toast_error,
    build_toast_sent,
)
from htmforge import render
from config import SECRET_KEY, CONTACT_TO, SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS, RATE_LIMIT_SECONDS

EMAIL_RE = re.compile(r"^[^\@\s]+@[^\@\s]+\.[^\@\s]+$")

app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 31536000
app.secret_key = SECRET_KEY

# Rate-Limit pro IP
CONTACT_RATE_LIMIT = {}

def _h(path: str) -> str:
    try:
        return hashlib.md5(open(path, "rb").read()).hexdigest()[:8]
    except FileNotFoundError:
        return "0"

def _hashes():
    return _h("static/css/main.css"), _h("static/js/main.js")

def _check_rate_limit(ip: str) -> bool:
    now = datetime.now()
    last = CONTACT_RATE_LIMIT.get(ip)
    if last and (now - last) < timedelta(seconds=RATE_LIMIT_SECONDS):
        return False
    CONTACT_RATE_LIMIT[ip] = now
    return True

@app.route("/")
def index():
    css, js = _hashes()
    return Response(build_home(css, js), mimetype="text/html")

@app.route("/kunden")
def kunden():
    css, js = _hashes()
    return Response(build_kunden_page(css, js), mimetype="text/html")

@app.route("/opensource")
def opensource():
    css, js = _hashes()
    return Response(build_opensource_page(css, js), mimetype="text/html")

@app.route("/software")
def software():
    css, js = _hashes()
    return Response(build_software_page(css, js), mimetype="text/html")

@app.route("/infra")
def infra():
    css, js = _hashes()
    return Response(build_infra_page(css, js), mimetype="text/html")

@app.route("/tarife")
def tarife():
    css, js = _hashes()
    return Response(build_tarife_page(css, js), mimetype="text/html")

@app.route("/kontakt")
def kontakt():
    css, js = _hashes()
    betreff = request.args.get("betreff", "")
    return Response(build_kontakt_page(css, js, betreff=betreff), mimetype="text/html")

@app.route("/kontakt/senden", methods=["POST"])
def kontakt_senden():
    ip = request.remote_addr
    if not _check_rate_limit(ip):
        return Response(render(build_toast_error(f"Zu viele Anfragen. Bitte {RATE_LIMIT_SECONDS} Sekunden warten.")), mimetype="text/html", status=429)
    
    name = (request.form.get("name") or "").strip()
    email = (request.form.get("email") or "").strip()
    betreff = (request.form.get("betreff") or "").strip()
    nachricht = (request.form.get("nachricht") or "").strip()
    honeypot = (request.form.get("website") or "").strip()

    if honeypot:
        return Response(render(build_kontakt_success()), mimetype="text/html")

    errors = {}
    if not name:
        errors["name"] = "Bitte Namen angeben."
    if not email or not EMAIL_RE.match(email):
        errors["email"] = "Bitte eine gültige E-Mail-Adresse angeben."
    if not nachricht or len(nachricht) < 10:
        errors["nachricht"] = "Bitte kurze Nachricht angeben (mind. 10 Zeichen)."

    if errors:
        html = render(build_kontakt_form(
            name=name, email=email, betreff=betreff, nachricht=nachricht, errors=errors,
        )) + render(build_toast_error("Bitte Angaben prüfen."))
        return Response(html, mimetype="text/html")

    sent = False
    if SMTP_USER and SMTP_PASS:
        try:
            msg = EmailMessage()
            msg["Subject"] = f"[NepiDesk Kontakt] {betreff or 'Anfrage'}"
            msg["From"] = SMTP_USER
            msg["To"] = CONTACT_TO
            msg["Reply-To"] = email
            msg.set_content(f"Name: {name}\nE-Mail: {email}\nBetrifft: {betreff}\n\n{nachricht}")
            with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as s:
                s.login(SMTP_USER, SMTP_PASS)
                s.send_message(msg)
            sent = True
        except Exception as exc:
            app.logger.error("Kontakt-Mail-Versand fehlgeschlagen: %s", exc)

    if sent:
        html = render(build_kontakt_success()) + render(build_toast_sent())
        return Response(html, mimetype="text/html")

    html = render(build_kontakt_form(
        name=name, email=email, betreff=betreff, nachricht=nachricht,
    )) + render(build_toast_error(f"Senden fehlgeschlagen — bitte direkt an {CONTACT_TO} schreiben."))
    return Response(html, mimetype="text/html")

@app.route("/impressum")
def impressum():
    css, js = _hashes()
    return Response(build_impressum_page(css, js), mimetype="text/html")

@app.route("/datenschutz")
def datenschutz():
    css, js = _hashes()
    return Response(build_datenschutz_page(css, js), mimetype="text/html")

@app.route("/toast/copy")
def toast_copy():
    return Response(render(build_toast_success()), mimetype="text/html")

@app.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")

@app.route("/sitemap.xml")
def sitemap():
    return send_from_directory("static", "sitemap.xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)