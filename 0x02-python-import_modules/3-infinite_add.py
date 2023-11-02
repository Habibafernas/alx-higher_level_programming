#!/usr/bin/python3

if __name__ == "__main__":
    import sys


    for i in range(len(sys.argv) - 1):
        t += sys.argv[i + 1]
    print("{}".format(t))
