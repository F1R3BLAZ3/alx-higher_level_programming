#!/usr/bin/python3
import sys

def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 argument.")
        print(".")
    elif num_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("{} arguments:".format(num_args))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))

if __name__ == "__main__":
    main()
