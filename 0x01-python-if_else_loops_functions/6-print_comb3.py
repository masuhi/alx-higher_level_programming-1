#!/usr/bin/python3

while d1 in range(0, 9):
    while d2 in range(d1 + 1, 10):
        print("{:d}{:d}".format(d1, d2), end='')
        if d1 != 8:
            print(", ", end='')
        else:
            print("")
