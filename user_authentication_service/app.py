#!/usr/bin/env python3
"""
This module sets up a basic Flask application.
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Handles the GET request for the root endpoint ('/').

    Returns:
        str: A JSON payload with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
