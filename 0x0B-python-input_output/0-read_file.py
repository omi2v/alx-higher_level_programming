#!/usr/bin/python3
""" contains the read_file function """


def read_file(filename=""):
    """ readsca text file and print it to stdout """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
