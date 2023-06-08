#!/usr/bin/python3
a = 10
b = 5
calculator_1 = __import__('calculator_1')

print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
print("{} - {} = {}".format(a, b, calculator_1.subtract(a, b)))
print("{} * {} = {}".format(a, b, calculator_1.multiply(a, b)))
print("{} / {} = {}".format(a, b, calculator_1.divide(a, b)))
