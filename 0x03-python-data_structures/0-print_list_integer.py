#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for idx in my_list:
        if type(idx) is int:
             print("{:d}".format(idx))
