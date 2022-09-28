#!/usr/bin/python3
""" contains the read_file function """
import json


def from_json_string(my_str):
    """ return jason of an object of string """
    return json.loads(my_str)
