#!/usr/bin/python
# Filename： print_func.py

# def print_func(par):
#     """Return the pathname of the KOS root directory."""

#     print('hello world')

#     print('中文')

#     return

# print_func("3");

def printinfo( name, age ):
    "打印任何传入的字符串"
    print("Name: %s"%name)
    print("Age %d"%age)
    return

printinfo( age=50, name="miki" )
printinfo("Randy",18)
printinfo("张登",1)
