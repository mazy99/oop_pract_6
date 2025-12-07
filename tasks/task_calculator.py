#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from calculator import Calculator, InputReader, ValueParser

if __name__ == "__main__":
    a_input = InputReader.read("Введите первое значение: ")
    b_input = InputReader.read("Введите второе значение: ")

    a_parsed = ValueParser.parse_int(a_input)
    b_parsed = ValueParser.parse_int(b_input)

    calculator = Calculator(a_parsed, b_parsed)
    print(calculator)
