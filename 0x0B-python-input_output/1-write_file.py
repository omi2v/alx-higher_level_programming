#!/usr/bin/python3
""" contains the read_file function """


def write_file(filename="", text=""):
    """ the with statement """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
