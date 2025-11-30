#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print("start")

try:
    val = int(input("Enter a number: "))
    tmp = 10 / val
    print(f"10 divided by {val} is {tmp}")

except ValueError as ve:
    print("ValueError: {0}".format(ve))

except ZeroDivisionError as zde:
    print("ZeroDivisionError: {0}".format(zde))

except Exception as ex:
    print("Error: {0}".format(ex))

print("stop")
