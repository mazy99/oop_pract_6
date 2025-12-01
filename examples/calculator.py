#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from typing import Union


class InputReader:

    @staticmethod
    def read(prompt: str) -> str:
        try:
            value = input(prompt)
        except Exception as e:
            print(f"Ошибка ввода: {e}")

        if value.strip() == "":
            raise ValueError("Пустое значение недопустимо")
        return value


class ValueParser:

    @staticmethod
    def parse_int(value: str) -> Union[float, str]:
        try:
            return float(value)
        except ValueError:
            return value


class Calculator:

    a: Union[int, float, str]
    b: Union[int, float, str]

    def __init__(self, a: Union[float, int, str], b: Union[float, int, str]) -> None:
        self.a = a
        self.b = b

    def calculate(self) -> Union[float, str]:
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)):
            return self.a + self.b
        return str(self.a) + str(self.b)

    def __str__(self) -> str:
        return f"Результат сложения: {self.calculate()}"


if __name__ == "__main__":
    a_input = InputReader.read("Введите первое значение: ")
    b_input = InputReader.read("Введите второе значение: ")

    a_parsed = ValueParser.parse_int(a_input)
    b_parsed = ValueParser.parse_int(b_input)

    calculator = Calculator(a_parsed, b_parsed)
    print(calculator)
