#!/usr/bin/python3
""" contains the read_file function """
import json


def load_from_json_file(filename):
    """ create an oobject from JSON """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
