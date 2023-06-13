#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    if num_args == 0:
        print("0 argument{}:".format("" if num_args == 0 else "s"))
        print(".")
    else:
        print("{} argument{}:".format(num_args, "" if num_args == 1 else "s"))
        for i, arg in enumerate(argv, 1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
