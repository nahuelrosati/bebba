from pathlib import Path
from flask import Flask, send_from_directory

BASE_DIR = Path(__file__).resolve().parent

app = Flask(__name__, static_folder=None)


@app.route("/")
def index():
    return send_from_directory(str(BASE_DIR), "index.html")


@app.route("/health")
def health():
    return {"status": "ok"}, 200