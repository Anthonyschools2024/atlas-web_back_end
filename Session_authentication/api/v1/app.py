#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views # Assuming app_views is correctly set up in api/v1/views/__init__.py
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os

# Initialize Flask app
app = Flask(__name__)
# Assuming app_views is a Blueprint instance.
# For this file to be self-contained for what it does,
# we'd need the definition of app_views or assume it's imported.
# from api.v1.views import app_views # This import is standard
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize auth to None
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

# Logic to initialize 'auth' based on AUTH_TYPE
# This part depends on your actual auth classes being available.
# For example, if AUTH_TYPE == "basic_auth":
#   from api.v1.auth.basic_auth import BasicAuth
#   auth = BasicAuth()
# If AUTH_TYPE == "session_auth":
#   from api.v1.auth.session_auth import SessionAuth
#   auth = SessionAuth()
# etc.
# For this snippet, we'll assume 'auth' is instantiated correctly elsewhere
# or we show the typical conditional loading:
if AUTH_TYPE == "auth": # Or a default Auth type from your 0x06 project
    from api.v1.auth.auth import Auth # Assuming this base class exists
    auth = Auth()
elif AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth # Assuming this class exists
    auth = BasicAuth()
# Add other auth types like session_auth if they are relevant from previous/future work


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler() -> None:
    """
    Handler executed before each request.
    Performs authentication checks.
    """
    if auth is None:
        return

    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
        # '/api/v1/auth_session/login/', # Example if session auth was being added
    ]

    if not auth.require_auth(request.path, excluded_paths):
        return

    # This condition might vary based on how 0x06 handled combined auth types
    # For Basic Auth, it's primarily the authorization_header.
    # If Session Auth was also part of 0x06 (unlikely given problem focus),
    # it would also check auth.session_cookie(request)
    if auth.authorization_header(request) is None: # and auth.session_cookie(request) is None:
        abort(401)
    
    # Assign the result of auth.current_user(request) to request.current_user
    # THIS IS THE KEY UPDATE FOR THIS TASK in app.py
    request.current_user = auth.current_user(request)
    
    if request.current_user is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    # The following imports would be needed if this file is run directly
    # and they set up User, Auth, BasicAuth classes for the auth logic to work.
    # from models.user import User (implicitly used by auth methods)
    # from api.v1.auth.auth import Auth
    # from api.v1.auth.basic_auth import BasicAuth
    app.run(host=host, port=port)
