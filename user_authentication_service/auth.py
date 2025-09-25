#!/usr/bin/env python3
"""
This module provides the authentication service logic.
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using the bcrypt algorithm.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as a byte string, including the salt.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """
    Auth class to interact with the authentication database.
    Manages user registration, login, and session handling.
    """

    def __init__(self) -> None:
        """
        Initializes a new Auth instance and creates a connection
        to the database.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user in the database.

        Args:
            email (str): The user's email address.
            password (str): The user's plaintext password.

        Returns:
            User: The newly created user object.

        Raises:
            ValueError: If the user's email already exists in the database.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            # Decode bytes to string for DB storage in VARCHAR column
            hashed_password_str = hashed_password.decode('utf-8')
            new_user = self._db.add_user(email, hashed_password_str)
            return new_user
