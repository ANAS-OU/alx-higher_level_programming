#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        rst = a ** b
    elif b == 0:
        rst = 1
    else:
        rst = 1 / (a ** abs(b))
    return (rst)
