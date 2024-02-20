#!/usr/bin/python3
MyList = __import__('1-my_list').MyList

try:
    my_list = MyList("hi", 22, "alx")
except Exception as e:
    print(e)

my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
try:
    my_list.append("hi")
except Exception as e:
    print(e)
print(my_list)
my_list.print_sorted()
print(my_list)
