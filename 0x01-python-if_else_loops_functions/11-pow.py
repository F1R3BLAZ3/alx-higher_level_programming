#!/usr/bin/python3
def pow(a, b):
    result = a ** b
    return int(result) if result.is_integer() else round(result, 2)
