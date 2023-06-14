#!/usr/bin/python3
import sys


def main():
    argv = sys.argv[1:]
    num_args = len(argv)

    print("Number of argument(s):", end=" ")
    if num_args == 0:
        print(".", end="\n\n")
    elif num_args == 1:
        print("1 argument:")
        print("1:", argv[0])
    else:
        print(num_args, "arguments:")
        for i, arg in enumerate(argv, 1):
            print(i, ":", arg)


if __name__ == "__main__":
    main()
