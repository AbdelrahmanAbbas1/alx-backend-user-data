#!/usr/bin/env python3
"""This module logs pbfuscates messages"""
import logging
import re
from typing import List, Dict

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log messa/>ge obfuscated"""
    patterns: Dict[str, str] = {key: f'{key}=[^{separator}]+'
                                for key in fields}
    for field, pattern in patterns.items():
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION: str = "***"
    FORMAT: str = (
        '[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s:%(message)s'
        )
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields: List[str] = fields

    def format(self, record: logging.LogRecord) -> str:
        """Returns the log message formatted"""
        record.msg = filter_datum(self.fields,
                                  self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """Returns a logging object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.propagate = False
    logger.addHandler(handler)
    return logger
