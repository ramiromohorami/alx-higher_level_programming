#!/usr/bin/python3
def search_replace(m_list, search, replace):
    return list(map(lambda e: replace if e == search else e, my_list))
