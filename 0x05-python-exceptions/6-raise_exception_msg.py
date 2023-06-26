#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                element_1 = my_list_1[i]
                element_2 = my_list_2[i]
                try:
                    result = element_1 / element_2
                    if not isinstance(result, (int, float)):
                        raise ValueError
                except ZeroDivisionError:
                    result = 0
                    print("division by 0")
                except ValueError:
                    result = 0
                    print("wrong type")
            except IndexError:
                result = 0
                print("out of range")
            finally:
                new_list.append(result)
    finally:
        return new_list
