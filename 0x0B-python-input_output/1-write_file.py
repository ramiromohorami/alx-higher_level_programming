#!/usr/bin/python3
"""function that writes a string"""


def write_file(filename="", text=""):
    """ module write_file"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
