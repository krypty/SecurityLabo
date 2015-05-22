# -*- coding: utf-8 -*-

REGEX_USER = "^[A-Za-z0-9]{4,}$"
REGEX_CHALLENGE = "^[A-Za-z]{8}$"

REGEX_HOST = "^[A-Za-z0-9.]{2,}$"

END_LINE = "\r\n"

BUFFER_SIZE = 512

def getMessage(code, value):
    return "%d %s%s" % (code, value, END_LINE)