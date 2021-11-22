#!/usr/bin/python3
def no_c(my_string):
    alt_string = ""
    x = 0
    while (x < len(my_string)):
        if my_string[x] != 'c' and my_string[x] != 'C':
            alt_string += my_string[x]
        x = x + 1
    my_string = alt_string
    return my_string
