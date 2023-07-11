#!/usr/bin/python3

"""
    Reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read
                        (default is an empty string).

    Returns:
        None
    """
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end='')


if __name__ == "__main__":
    read_file()
