#!/usr/bin/python3

new = []


sum = 0
def uniq_add(my_list=[]):
    for i in my_list:
        if i not in new:
            sum += i
            new.append(i)
    return sum
