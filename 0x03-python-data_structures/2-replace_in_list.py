#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    for element in my_list:
        if (idx < 0):
            return my_list
        elif i == idx:
            my_list.insert(idx, element)
            return my_list
        i += 1
    return None
