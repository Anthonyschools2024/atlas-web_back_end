#!/usr/bin/env python3
"""
Module for filtering PII data from log messages.
Contains a function to obfuscate specified fields,
a Formatter class to integrate this into logging,
and a function to retrieve a configured logger for user data.
"""
import re
from typing import List, Tuple
import logging

# Define PII_FIELDS constant at the root of the module.
# These are fields considered PII and will be redacted by the logger.
PII_FIELDS: Tuple[str, str, str, str, str] = ("name", "email", "phone", "ssn", "password")


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
        record.msg = filter_datum(fields=self.fields,
                                  redaction=self.REDACTION,
                                  message=record.msg,
                                  separator=self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and returns a configured logger for user data.

    The logger is named "user_data", logs messages up to the INFO level,
    and does not propagate messages to parent loggers. It is equipped
    with a StreamHandler that uses the RedactingFormatter, parameterized
    by the PII_FIELDS constant, to redact sensitive information.

    Returns:
        logging.Logger: A configured logger instance for user data.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Do not propagate messages to other loggers

    # Create a StreamHandler to output logs to the console (or other stream)
    stream_handler = logging.StreamHandler()

    # Create an instance of RedactingFormatter, parameterized with PII_FIELDS.
    # RedactingFormatter's __init__ expects a List[str] for fields.
    formatter = RedactingFormatter(fields=list(PII_FIELDS))

    # Set the formatter for the StreamHandler
    stream_handler.setFormatter(formatter)

    # Add the handler to the logger, ensuring it's not added multiple times
    # if get_logger is called repeatedly for the same logger instance.
    if not logger.handlers:
        logger.addHandler(stream_handler)

    return logger
