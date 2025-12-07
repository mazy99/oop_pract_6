#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matrix_generate import MatrixGenerator


def main():
    try:
        rows = int(input("Введите количество строк матрицы: "))
        cols = int(input("Введите количество столбцов матрицы: "))

        if rows <= 0 or cols <= 0:
            raise ValueError("Количество строк и столбцов должно быть положительным.")

        min_value = int(input("Введите минимальное значение элемента матрицы: "))
        max_value = int(input("Введите максимальное значение элемента матрицы: "))

        if min_value > max_value:
            raise ValueError("Минимальное значение не может быть больше максимального.")

        generator = MatrixGenerator(rows, cols, min_value, max_value)
        print(generator)
    except ValueError as ve:
        print(f"Ошбибка ввода: {ve}")
        return


if __name__ == "__main__":
    main()
