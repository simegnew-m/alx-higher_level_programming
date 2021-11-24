#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mydict = a_dictionary.copy()
    for i in mydict.keys():
        mydict[i] = mydict[i] * 2
    return mydict
