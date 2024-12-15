#!/usr/bin/env python3
""""This module obfuscate the log message"""
import re


def filter_datum(fields, redaction, message, separator):
    """returns the log messa/>ge obfuscated"""
    patterns = {key: f'{key}=[^{separator}]' for key in fields}
    for field, pattern in patterns.items():
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
