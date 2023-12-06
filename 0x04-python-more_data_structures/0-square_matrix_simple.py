#!/usr/bin/python3
def square_matric_simple(matrix=[]):
    return list(map(lambda sub: list(map(lambda e: e**2, sub)), matrix))
