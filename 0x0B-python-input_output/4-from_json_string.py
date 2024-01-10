#!/usr/bin/python3
"""function that returns an object (Python data structure)"""

import json


def from_json_string(my_str):
    """module from_json_string"""
    return json.loads(my_str)
