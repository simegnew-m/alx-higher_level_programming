#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0:
            print("Fizz", end='')
        if x % 5 == 0:
            print("Buzz", end='')
        if x % 3 and x % 5:
            print("{:d}".format(x), end='')
        print(end=' ')
