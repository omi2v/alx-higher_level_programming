#!/usr/bin/python3
""" contains the read_file function """


def class_to_json(obj):
    """ a function that return a dictionary using json """
    return obj.__dict__
