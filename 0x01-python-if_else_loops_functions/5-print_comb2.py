#!/usr/bin/python3
# To write a program that prints numbers from 0 to 99
for i in range(0, 99):
    print("{:0>2d}".format(i), end=", ")
print(i+1)
