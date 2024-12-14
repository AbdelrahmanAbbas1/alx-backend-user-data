#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    patterns = {
        'email': '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'password': '^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$'
        }
    mod = message.split(';')
    pairs = mod[:-1]
    dict_message = {key: value for key, value in (pair.split('=') for pair in pairs)}
    for field in fields:
        if field in dict_message:
            mes = dict_message[field]
            l = re.sub(patterns[field], redaction, mes)
            print(l)

fields = ["password", "date_of_birth"]
messages = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"

filter_datum(fields, 'xxx', messages, ';')