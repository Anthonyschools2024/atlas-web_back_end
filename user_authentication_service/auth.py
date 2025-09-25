#!/usr/bin/env python3
"""
This module provides the authentication service logic.
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound
from typing import Optional

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


def _generate_uuid() -> str:
    """
    Generates a new random UUID (version 4).

    Returns:
        str: The string representation of the UUID.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user's login credentials.

        Args:
            email (str): The user's email.
            password (str): The user's password.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        password_bytes = password.encode('utf-8')
        hashed_password_bytes = user.hashed_password.encode('utf-8')

        return bcrypt.checkpw(password_bytes, hashed_password_bytes)

    def create_session(self, email: str) -> Optional[str]:
        """
        Creates a new session for a user.

        Args:
            email (str): The user's email address.

        Returns:
            Optional[str]: The session ID string if the user is found,
                           otherwise None.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        Retrieves a user based on their session ID.

        Args:
            session_id (str): The session ID of the user.

        Returns:
            Optional[User]: The User object if found, otherwise None.
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys a user's session, effectively logging them out.

        Args:
            user_id (int): The ID of the user whose session is to be destroyed.
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a reset password token for a user.

        Args:
            email (str): The email of the user requesting a reset.

        Returns:
            str: The reset password token.

        Raises:
            ValueError: If the email is not registered to a user.
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError("User not found")
