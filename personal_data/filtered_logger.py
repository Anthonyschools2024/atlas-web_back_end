#!/usr/bin/env python3
"""
Module for filtering PII data from log messages.
Contains a function to obfuscate specified fields in a log string.
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message with specified fields obfuscated.

    This function uses a single regular expression substitution to find and
    replace the values of fields specified in the `fields` list with the
    `redaction` string.

    Args:
        fields (List[str]): A list of strings representing all field names
                              to obfuscate (e.g., ["password", "ssn"]).
        redaction (str): A string representing by what the field value
                         will be obfuscated (e.g., "***").
        message (str): A string representing the log line. Log lines are
                       expected to be a series of 'key=value' pairs
                       separated by `separator`.
        separator (str): A string representing the character that separates
                         all fields in the log line (e.g., ";").

    Returns:
        str: The log message with specified fields obfuscated.
             Example: "name=user;password=secret;" -> "name=user;password=***;"
    """
    # Construct a regex pattern that matches any of the specified fields
    # followed by an equals sign and its value.
    # The pattern (field1|field2|...)=[^separator]* does the following:
    #   - (field1|field2|...): Captures the field name (group 1). This allows
    #     us to refer to it in the replacement string using \1.
    #   - =: Matches the literal equals sign.
    #   - [^separator]*: Matches any sequence of characters that are not the
    #     separator, effectively capturing the field's value.
    # The replacement string fr"\1={redaction}" uses the captured field name (\1),
    # adds an equals sign, and then appends the redaction string.
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, fr"\1={redaction}", message)
