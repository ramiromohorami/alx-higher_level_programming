#!/usr/bin/python3
"""
function that inserts a line of text to a file, after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    '''module Search and update
    '''
    with open(filename, 'r+') as f:
        rows = f.readlines()
        i = 0
        for row in rows:
            if row.find(search_string) is not -1:
                rows.insert(i + 1, new_string)
            i += 1
        f.seek(0)
        f.write("".join(rows))
