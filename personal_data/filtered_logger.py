#!/usr/bin/env python3
"""
Module for filtering PII data from log messages.
Contains a function to obfuscate specified fields in a log string
and a Formatter class to integrate this into logging.
"""
import re
from typing import List
import logging


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
    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(pattern, fr"\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class that filters specified PII fields
        from log messages before standard formatting.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the RedactingFormatter.

        Args:
            fields (List[str]): A list of strings representing the names
                                of fields to redact in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, redacting specified PII fields in the message
        before applying the overall log format.

        The method modifies `record.msg` by applying `filter_datum` and then
        calls the parent class's `format` method to produce the final string.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log string.
        """
        # Redact the message part of the log record using filter_datum.
        # record.msg contains the raw message string (assuming record.args is not used,
        # as in the provided example).
        record.msg = filter_datum(fields=self.fields,
                                  redaction=self.REDACTION,
                                  message=record.msg,
                                  separator=self.SEPARATOR)
        # Call the parent class's format method to apply FORMAT.
        return super().format(record)
