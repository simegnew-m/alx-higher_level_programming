#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ''
    if n > len(str) or n < 0:
        return str
    for c in str:
        if c != str[n]:
            str2 += c
    return str2
