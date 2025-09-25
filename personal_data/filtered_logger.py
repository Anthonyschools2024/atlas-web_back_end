#!/usr/bin/env python3
"""
Module for filtering and obfuscating sensitive log data.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns a log message with specified fields obfuscated.

    Args:
        fields (List[str]): A list of strings representing fields to obfuscate.
        redaction (str): The string to replace the field value with.
        message (str): The log line to process.
        separator (str): The character separating fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
