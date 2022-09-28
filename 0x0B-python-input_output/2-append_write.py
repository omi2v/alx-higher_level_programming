#!/usr/bin/python3
""" contains the read_file function """


def append_write(filename="", text=""):
    """ appending to a file """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
