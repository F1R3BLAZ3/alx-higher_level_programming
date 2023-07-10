#!/usr/bin/python3

"""
A custom list class that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from list.

    Public Methods:
        print_sorted(self): Prints the list in sorted (ascending) order.
    """

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
