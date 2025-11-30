#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class NegValException(Exception):
    pass


try:
    val = int(input("Enter a positive number: "))
    if val < 0:
        raise NegValException(f"Negative value entered {val}")
    print(f"val + 10 = {val+10}")
except NegValException as nve:
    print(f"NegValException: {nve}")
