#!/usr/bin/python3
def uppercase(str):
    """print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 124:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")    
