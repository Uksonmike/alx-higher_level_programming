#!/usr/bin/python3
"""
This module is all about learning to write
a string to text file in UTF8 and return the numbers of characters
"""


def write_file(filename="", text=""):
    """"write a file """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
