#!/usr/bin/python3
from calculator_1 import sum, diff, mul, div
def main():
    x = 10
    y = 5
    print("{} + {} = {}".format(x, y, sum(x, y)))
    print("{} - {} = {}".format(x, y, diff(x, y)))
    print("{} * {} = {}".format(x, y, mul(x, y)))
    print("{} / {} = {}".format(x, y, div(x, y)))

if __name__ == "__main__":
    main
