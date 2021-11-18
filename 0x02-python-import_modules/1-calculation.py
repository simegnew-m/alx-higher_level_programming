#!/usr/bin/python3
from calculator_1 import sum, diff, mul, div

def main():
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, sum(a, b)))
    print("{} - {} = {}".format(a, b, diff(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))

if __name__ == "__main__":
    main()
