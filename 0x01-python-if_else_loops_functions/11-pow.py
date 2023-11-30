#!/usr/bin/python3
def pow(a, b):
    rst = 1
    if b > 0:
        for i in range(b):
            rst *= a
    elif b < 0:
        for i in range(abs(b)):
            rst *= 1 / a
    return (rst)
