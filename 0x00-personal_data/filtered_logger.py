#!/usr/bin/env python3
""""This module obfuscate the log message"""
import re
from typing import List, Dict


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log messa/>ge obfuscated"""
    patterns: Dict[str: str] = {key: f'{key}=[^{separator}]' for key in fields}
    for field, pattern in patterns.items():
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
