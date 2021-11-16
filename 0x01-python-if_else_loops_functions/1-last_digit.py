#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# if the number is negative, divide the number by -10 to get the last digit
# if the number is positive, divide the number by 10 to get the last digit
if number < 0:
    r = number % -10
else:
    r = number % 10
# if the last digit is greater than 5: the string and is greater than 5
# if the last digit is 0: the string and is 0
# if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
print('Last digit of', number, 'is', r, end=' ')
if r > 5:
    print('and is greater than 5')
elif r == 0:
    print('and is 0')
else:
    print('and is less than 6 and not 0')
