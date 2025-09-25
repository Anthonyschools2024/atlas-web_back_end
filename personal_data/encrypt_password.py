#!/usr/bin/env python3
"""
Module for handling password encryption and validation using the bcrypt library.
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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if a plain-text password matches a bcrypt hashed password.

    Args:
        hashed_password (bytes): The stored hash to check against.
        password (str): The plain-text password to validate.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # Encode the plain-text password to bytes
    password_bytes = password.encode('utf-8')

    # bcrypt.checkpw handles extracting the salt and comparing the hashes
    return bcrypt.checkpw(password_bytes, hashed_password)
