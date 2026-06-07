"""
NepiDesk — nepidesk.de
Flask App. Nur Routes.
"""

import hashlib
from flask import Flask, Response
from components import build_home, build_ssh_page, build_nas_page, build_toast_success
from htmforge import render

app = Flask(__name__, static_folder="static")


def _h(path: str) -> str:
    try:
        return hashlib.md5(open(path, "rb").read()).hexdigest()[:8]
    except FileNotFoundError:
        return "0"


@app.route("/")
def index():
    return Response(build_home(_h("static/css/main.css"), _h("static/js/main.js")), mimetype="text/html")


@app.route("/ssh")
def ssh():
    return Response(build_ssh_page(_h("static/css/main.css"), _h("static/js/main.js")), mimetype="text/html")


@app.route("/nas")
def nas():
    return Response(build_nas_page(_h("static/css/main.css"), _h("static/js/main.js")), mimetype="text/html")


@app.route("/toast/copy")
def toast_copy():
    return Response(render(build_toast_success()), mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)