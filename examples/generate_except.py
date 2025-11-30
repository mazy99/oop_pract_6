#!/usr/bin/env python3
# -*- coding: utf-8 -*-


try:
    raise Exception("Some exception message")

except Exception as e:
    print(f"Exception: {e}")
