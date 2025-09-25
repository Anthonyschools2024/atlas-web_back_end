#!/usr/bin/env python3
"""
This module sets up a basic Flask application.
"""
from flask import Flask, jsonify, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Handles the GET request for the root endpoint ('/').

    Returns:
        str: A JSON payload with a welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """
    Handles the POST request for the /users endpoint to register a user.

    Form data:
        - email (str): The user's email address.
        - password (str): The user's password.

    Returns:
        str: A JSON payload indicating success or failure.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        payload = {"email": user.email, "message": "user created"}
        return jsonify(payload)
    except ValueError:
        payload = {"message": "email already registered"}
        return jsonify(payload), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Handles the POST request for the /sessions endpoint to log a user in.

    Form data:
        - email (str): The user's email address.
        - password (str): The user's password.

    Returns:
        str: A JSON payload indicating success or an aborts with a 401 status.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
