#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, element in enumerate(row):
            print("{:d}".format(element), end=" ")
        print()
