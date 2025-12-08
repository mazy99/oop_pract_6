#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("start")

try:
    val = int(input("Enter a number: "))
    tmp = 10 / val
    print(f"10 divided by {val} is {tmp}")

except ValueError as ve:
    print(f"ValueError: {ve}")

except ZeroDivisionError as zde:
    print(f"ZeroDivisionError: {zde}")

except Exception as ex:
    print(f"Error: {ex}")

print("stop")
