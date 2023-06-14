#!/usr/bin/python3


def uniq_add(my_list=[]):
    unique_set = set(my_list)  # Convert list to a set to remove duplicates
    sum_unique = sum(unique_set)  # Sum all unique integers
    return sum_unique
