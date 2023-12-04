#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for inside in matrix:
        if len(inside) == 0:
            print()
        for elem in range(len(inside)):
            print("{:d}".format(inside[elem]),
                  end="\n" if elem is len(inside) - 1 else " ")
