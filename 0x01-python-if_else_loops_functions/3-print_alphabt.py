#!/usr/bin/python3
# To write a program that prints the ASCII alphabet, in lowercase
for i in range(ord('a'), ord('z') + 1):
# To print all the letters except q and e
    if i != ord('e') and i != ord('q'):
        print("{:c}".format(i), end="")
