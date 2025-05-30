ls#!/usr/bin/env python3
"""
Module for PII data handling, including log filtering,
logger configuration, and secure database connections.
"""
import re
from typing import List, Tuple
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


# Define PII_FIELDS constant at the root of the module.
# These are fields considered PII and will be redacted by the logger.
PII_FIELDS: Tuple[str, str, str, str, str] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    Args:
        fields (List[str]): A list of strings representing all field names
                              to obfuscate.
        redaction (str): A string representing by what the field value
                         will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing the character that separates
                         all fields in the log line.

    Returns:
        str: The log message with specified fields obfuscated.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, fr"\1={redaction}", message)


