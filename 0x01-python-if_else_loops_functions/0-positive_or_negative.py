#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# if number is greater than 0: is positive
# if number is 0: is zero
# if number is less than 0: is negative
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
