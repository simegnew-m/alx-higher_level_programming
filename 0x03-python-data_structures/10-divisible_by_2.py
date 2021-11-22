#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lists = []
for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            lists.append(True)
        else:
            lists.append(False)
    return (lists)
