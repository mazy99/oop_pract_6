#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest

from tasks.calculator import Calculator, InputReader, ValueParser


@pytest.mark.parametrize(
    "input_str, expected",
    [("10", 10), ("-5", -5), ("3.14", 3.14), ("0", 0), ("abc", "abc"), ("12.0", 12.0)],
)
def test_parse_int(input_str, expected):
    assert ValueParser.parse_int(input_str) == expected


def test_calculator_numbers():
    calc = Calculator(5, 7)
    assert calc.calculate() == 12
    assert str(calc) == "Результат сложения: 12"


def test_calculator_floats():
    calc = Calculator(3.5, 2.5)
    assert calc.calculate() == 6.0
    assert str(calc) == "Результат сложения: 6.0"


def test_calculator_string_and_number():
    calc = Calculator("abc", 5)
    assert calc.calculate() == "abc5"
    assert str(calc) == "Результат сложения: abc5"


def test_calculator_two_strings():
    calc = Calculator("foo", "bar")
    assert calc.calculate() == "foobar"
    assert str(calc) == "Результат сложения: foobar"


def test_input_reader_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "test")
    result = InputReader.read("Введите что-то: ")
    assert result == "test"


def test_input_reader_empty(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "   ")
    with pytest.raises(ValueError) as excinfo:
        InputReader.read("Введите что-то: ")
    assert "Пустое значение недопустимо" in str(excinfo.value)
