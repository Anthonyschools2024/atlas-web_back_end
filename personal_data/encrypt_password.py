#!/usr/bin/env python3
"""
Module for handling password encryption using the bcrypt library.

Provides a function to take a plain-text password and return
a salted and hashed version suitable for secure storage.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.

    The function takes a plain-text password, encodes it to UTF-8,
    generates a random salt, and then uses bcrypt's hashpw function
    to create a secure, salted hash.

    Args:
        password (str): The plain-text password string to hash.

    Returns:
        bytes: The salted and hashed password as a byte string.
               Each call will produce a different result due to the
               random salt generation, but all will be valid for
               the same input password.
    """
    # Encode the password string into bytes (UTF-8 is standard)
    password_bytes = password.encode('utf-8')

    # Generate a new salt for each password hash
    # bcrypt.gensalt() handles creating a salt with an appropriate work factor
    salt = bcrypt.gensalt()

    # Hash the password bytes with the generated salt
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password
