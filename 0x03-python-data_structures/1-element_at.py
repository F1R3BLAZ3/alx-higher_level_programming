#!/usr/bin/python3
def element_at(my_list, idx):
    i = 0
    for element in my_list:
        if (idx < 0):
            return None
        elif i == idx:
            return element
        i += 1
    return None
