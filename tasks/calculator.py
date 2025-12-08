#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
    def parse_int(value: str) -> int | float | str:
        try:
            if "." in value:
                return float(value)
            return int(value)
        except ValueError:
            return value


class Calculator:

    a: int | float | str
    b: int | float | str

    def __init__(self, a: int | float | str, b: int | float | str) -> None:
        self.a = a
        self.b = b

    def calculate(self) -> int | float | str:
        if isinstance(self.a, (int, float)) and isinstance(self.b, (int, float)):
            return self.a + self.b
        return str(self.a) + str(self.b)

    def __str__(self) -> str:
        return f"Результат сложения: {self.calculate()}"
