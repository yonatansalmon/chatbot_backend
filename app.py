import threading
import time
import json

from flask import Flask, jsonify, render_template, request, redirect

count = 2

books = [
    {
        "id": 1,
        "title": "Harry Potter",
        "author": "JK Rowling",
        "published": "1997"
    },
    {
        "id": 2,
        "title": "Lord of the rings",
        "author": "JRR Tolkien",
        "published": "1954"
    },
]

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_books():
    return 'hello world'
    # return render_template('show_books.html', books=books)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    time.sleep(0.5)
    threading.Thread(target=app.run).start()
