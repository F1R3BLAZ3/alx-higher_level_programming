#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two elements from each tuple or use 0 if the tuple is smaller than 2
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    # Compute the sum of corresponding elements
    sum_1 = a1 + b1
    sum_2 = a2 + b2

    # Return a new tuple with the sum of elements
    return (sum_1, sum_2)
