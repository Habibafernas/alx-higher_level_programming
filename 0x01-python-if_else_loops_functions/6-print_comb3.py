#!/usr/bin/python3
for i in range(1, 90):
    if i not in range(10, 12) or i not in range(20, 23) or i not in range(30, 34) or i not in range(40,45) or i not in range(50, 56) or i not in range(60, 67) or i not in range(70, 78) or i not in range(80, 89):
        print("{:02}".format(i), end=", ")
    elif i == 89:
        print("{:02}".format(i))
