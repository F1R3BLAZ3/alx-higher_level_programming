#!/usr/bin/python3
def main():
    import add_0
    a = 1
    b = 2
    result = add_0.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))

if __name__ == "__main__":
    main()
