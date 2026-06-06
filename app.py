"""
belchenstrasse5.de — Flask App
Nur Routes. Kein HTML, kein CSS, kein Template.
"""

import hashlib
from flask import Flask, Response
from components import build_page, build_toast_success
from htmforge import render

app = Flask(__name__, static_folder="static")


def _file_hash(path: str) -> str:
    try:
        with open(path, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()[:8]
    except FileNotFoundError:
        return "0"


@app.route("/")
def index():
    css_h = _file_hash("static/css/main.css")
    js_h  = _file_hash("static/js/main.js")
    return Response(build_page(css_h, js_h), mimetype="text/html")


@app.route("/toast/copy")
def toast_copy():
    return Response(render(build_toast_success()), mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)