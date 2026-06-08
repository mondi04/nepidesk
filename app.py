"""
NepiDesk — nepidesk.de
Flask App. Nur Routes.
"""

import hashlib
from flask import Flask, Response, send_from_directory
from components import (
    build_home,
    build_ssh_page,
    build_nas_page,
    build_toast_success,
    build_opensource_page,
    build_software_page,
    build_infra_page,
    build_impressum_page,
    build_datenschutz_page,
)
from htmforge import render

app = Flask(__name__, static_folder="static")


def _h(path: str) -> str:
    try:
        return hashlib.md5(open(path, "rb").read()).hexdigest()[:8]
    except FileNotFoundError:
        return "0"


def _hashes():
    return _h("static/css/main.css"), _h("static/js/main.js")


@app.route("/")
def index():
    css, js = _hashes()
    return Response(build_home(css, js), mimetype="text/html")


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


@app.route("/impressum")
def impressum():
    css, js = _hashes()
    return Response(build_impressum_page(css, js), mimetype="text/html")


@app.route("/datenschutz")
def datenschutz():
    css, js = _hashes()
    return Response(build_datenschutz_page(css, js), mimetype="text/html")


@app.route("/ssh")
def ssh():
    css, js = _hashes()
    return Response(build_ssh_page(css, js), mimetype="text/html")


@app.route("/nas")
def nas():
    css, js = _hashes()
    return Response(build_nas_page(css, js), mimetype="text/html")


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