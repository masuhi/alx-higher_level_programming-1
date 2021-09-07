#!/usr/bin/python3
endStr = ", "

for k in range(0, 100):
    if k == 99:
        endStr = ""
    print("{:02d}".format(k), end=endStr)
print('')
