#!/usr/bin/env python3
"""
This module provides the authentication service logic.
"""
import bcrypt


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
