#!/usr/bin/env python3
"""
A script that connects to a secure database, retrieves user data,
and logs it with sensitive information redacted.
"""
import re
import os
import logging
import mysql.connector
from typing import List

PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the formatter.

        Args:
            fields (List[str]): A list of strings representing fields to obfuscate.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using filter_datum.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted and redacted log string.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger named 'user_data'.

    Returns:
        logging.Logger: A configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Creates and returns a connector to a secure MySQL database.

    Reads database credentials from environment variables.

    Returns:
        A mysql.connector.connection.MySQLConnection object.
    """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    db_connection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
    return db_connection


def main() -> None:
    """
    Retrieves user data from a database and logs it with PII fields redacted.
    """
    db = get_db()
    cursor = db.cursor()
    logger = get_logger()

    cursor.execute("SELECT * FROM users;")
    column_names = [desc[0] for desc in cursor.description]

    for row in cursor:
        message = "; ".join(f"{name}={val}" for name, val in zip(column_names, row))
        logger.info(message + ';')

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
