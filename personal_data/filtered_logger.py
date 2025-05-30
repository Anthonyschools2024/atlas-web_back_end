#!/usr/bin/env python3
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

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log string.
        """
        # Modify record.msg directly as it's used by record.getMessage()
        # if record.args is None, as in the typical use case here.
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

    stream_handler = logging.StreamHandler()
    # RedactingFormatter's __init__ expects a List[str] for fields.
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    # Add handler only if no handlers are configured to avoid duplicates
    if not logger.handlers:
        logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    """
    Establishes a connection to a MySQL database using credentials
    from environment variables and returns the connection object.

    Environment Variables Used:
    - PERSONAL_DATA_DB_USERNAME: Database username (default: "root")
    - PERSONAL_DATA_DB_PASSWORD: Database password (default: "")
    - PERSONAL_DATA_DB_HOST: Database host (default: "localhost")
    - PERSONAL_DATA_DB_NAME: Database name. This variable must be set in
                             the environment to connect to a specific database.
                             This function does not assign a default database name
                             if the variable is not set.

    Returns:
        mysql.connector.connection.MySQLConnection: A connection object to the database.
    """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    # Per instructions, PERSONAL_DATA_DB_NAME is fetched; no default for it
    # is specified for the os.environ.get() call itself in the problem description.
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    # Establish and return the database connection
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=host,
                                  database=db_name)
    return cnx
