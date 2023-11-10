#!/usr/bin/python3


def uniq_add(my_list=[]):
    new = []
    sum = 0
    for i in my_list:
        if i not in new:
            sum += i
            new.append(i)
    return sum
