#!/usr/bin/python3
""" contains the read_file function """
import json


def save_to_json_file(my_obj, filename):
    """ a function that write an object too text using json """
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
