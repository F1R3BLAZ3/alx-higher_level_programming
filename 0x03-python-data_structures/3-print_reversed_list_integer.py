#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for element in my_list:
        if isinstance(element, int):
            print("{:d}".format(my_list[element]))
