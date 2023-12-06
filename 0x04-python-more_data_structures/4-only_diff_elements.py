#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    od_set = set()
    for element in set_1:
        for element in set_2:
            od_set = set_1.union(set_2)
    return od_set

