#!/usr/bin/env python3
def no_c(my_string):
    for i in range(my_string):
        if my_string[i] == "c" or my_string == "C":
            my_string[i] = ""
    return my_string
