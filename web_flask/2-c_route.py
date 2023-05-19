#!/usr/bin/python3
"""Starts a flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Returns the home page"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns the hbnb page"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Returns a custom page"""
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
