#!/usr/vin/python3
def remove_char_at(str, n):
    string2 = ""
    for i, c in enumerate(str):
        if i != n:
            string2 += c
    return string2
