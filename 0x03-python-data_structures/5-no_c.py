#!/usr/bin/python3
def no_c(my_string):
    for i in range(my_string):
        if my_string[i] == "c" or my_string[i] == "C":
            string = my_string.translate({ord(i): None for i in 'cC'})
    return string
