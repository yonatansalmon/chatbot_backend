import threading
import time
import json
import os

from flask import Flask, jsonify, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_books():
    return 'hello world'


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    time.sleep(0.5)
    local = "127.0.0.1"
    heroku = "0.0.0.0"
    port = int(os.environ.get("PORT", 5000))
    app.run(host=heroku, port=port)
