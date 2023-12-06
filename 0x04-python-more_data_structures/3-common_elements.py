#!/usr/bin/python3
def common_elements(set_1, set_2):
    C_set = set()
    for i in set_1:
        for j in set_2:
            if i == j:
                C_set.add(i)
    return C_set
