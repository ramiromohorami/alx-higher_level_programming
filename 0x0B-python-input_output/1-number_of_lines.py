#!/usr/bin/python3
''' function that returns the number of lines of a text file
'''


def number_of_lines(filename=""):
    ''' function: number_of_lines
    '''
    if filename == "" or type(filename) != str:
        return 0
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
