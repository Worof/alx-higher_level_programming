#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_str += chr(ord(char) - 32)
        else:
            uppercase_str += char
    print("{}".format(uppercase_str))
