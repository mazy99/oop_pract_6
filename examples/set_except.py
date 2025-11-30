#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("start")

try:
    val = int(input("Enter a number: "))
    tmp = 10 / val
    print(f"10 divided by {val} is {tmp}")

except (ValueError, ZeroDivisionError):
    print("Error")
print("end")
