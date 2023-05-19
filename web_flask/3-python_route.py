#!/usr/bin/python3
"""Starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text: str):
    return "C " + text.replace('_', ' ')


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="cool"):
    return "Python is " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
