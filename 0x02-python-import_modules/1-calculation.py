#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as my_module

a = 10
b = 5

rst = my_module.add(a, b)
print("{} + {} = {}".format(a, b, rst))

rst = my_module.sub(a, b)
print("{} - {} = {}".format(a, b, rst))

rst = my_module.mul(a, b)
print("{} * {} = {}".format(a, b, rst))

rst = my_module.div(a, b)
print("{} / {} = {}".format(a, b, rst))
