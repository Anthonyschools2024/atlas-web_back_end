#!/usr/bin/env python3
"""
Module for handling password encryption using the bcrypt library.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a randomly generated salt.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        bytes: The salted and hashed password as a byte string.
    """
    # Encode the string password into bytes, as required by bcrypt
    password_bytes = password.encode('utf-8')

    # Generate a salt. gensalt() creates a new random salt for each call.
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
