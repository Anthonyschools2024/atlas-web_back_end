#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views # Assuming app_views Blueprint is defined
from flask import abort, jsonify, request
from models.user import User # Assuming User model is available

# This file assumes 'app_views' is a Flask Blueprint imported from api.v1.views
# and 'User' model is correctly defined and can be imported.

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users() -> str:
    """ GET /api/v1/users
    Return:
      - list of all User objects JSON represented
    """
    # This assumes User.all() and user.to_json() methods exist from 0x06
    all_users = [user.to_json() for user in User.all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_user(user_id: str = None) -> str:
    """ GET /api/v1/users/:id
        or GET /api/v1/users/me (if authenticated)
    Path parameter:
      - user_id: (string) User ID or "me"
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist or if user_id is "me" and user is not authenticated
    """
    # THIS IS THE KEY UPDATE FOR THIS TASK in users.py
    if user_id == "me":
        # request.current_user is populated by the @app.before_request in app.py
        if request.current_user is None:
            abort(404)  # As per prompt
        else:
            # User is authenticated, return their details
            # Assumes request.current_user is a User object with a to_json() method
            return jsonify(request.current_user.to_json())

    # This assumes User.get(user_id) and user.to_json() methods exist from 0x06
    user = User.get(user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_json())


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_user(user_id: str = None) -> str:
    """ DELETE /api/v1/users/:id
    Path parameter:
      - User ID
    Return:
      - empty JSON is the User has been correctly deleted
      - 404 if the User ID doesn't exist
    """
    # Assumes User.get(user_id) and user.remove() methods exist
    user = User.get(user_id)
    if user is None:
        abort(404)
    user.remove()
    return jsonify({}), 200


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user() -> str:
    """ POST /api/v1/users/
    JSON body:
      - email
      - password
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 400 if can't create the new User
    """
    try:
        rj = request.get_json()
    except Exception as e:
        abort(400, description="Not a JSON")

    if rj is None:
        abort(400, description="Not a JSON")
    if rj.get("email") is None:
        abort(400, description="email missing")
    if rj.get("password") is None:
        abort(400, description="password missing")

    try:
        # Assumes User class can be instantiated and has attributes/methods:
        # email, password (setter), first_name, last_name, save(), to_json()
        user = User()
        user.email = rj.get("email")
        user.password = rj.get("password")
        user.first_name = rj.get("first_name")
        user.last_name = rj.get("last_name")
        user.save()
        return jsonify(user.to_json()), 201
    except Exception as e:
        abort(400, description="Can't create User: {}".format(e))


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id: str = None) -> str:
    """ PUT /api/v1/users/:id
    Path parameter:
      - User ID
    JSON body:
      - last_name (optional)
      - first_name (optional)
    Return:
      - User object JSON represented
      - 404 if the User ID doesn't exist
      - 400 if can't update the User
    """
    # Assumes User.get(user_id) exists
    user = User.get(user_id)
    if user is None:
        abort(404)
    
    try:
        rj = request.get_json()
    except Exception as e:
        abort(400, description="Not a JSON")

    if rj is None:
        abort(400, description="Not a JSON")

    # Assumes User object has first_name, last_name attributes and save(), to_json() methods
    if 'first_name' in rj:
        user.first_name = rj.get('first_name')
    if 'last_name' in rj:
        user.last_name = rj.get('last_name')
    user.save()
    return jsonify(user.to_json()), 200
