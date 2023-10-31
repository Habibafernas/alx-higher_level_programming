#!/usr/bin/python3
for i in range(0, 90):
    if i not in range(10, 12) or i in range(20, 23) or i in range(30, 34) or i in range(40,45) or i in range(50, 56) or i in range(60, 67) or i in range(70, 78) or i in range(80, 89):
        print("{:02}".format(i), end=",")
    elif i == 89:
        print("{:02}".format(i))
