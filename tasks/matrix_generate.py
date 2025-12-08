#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


class MatrixGenerator:
    def __init__(self, rows: int, cols: int, min_value: int, max_value: int) -> None:
        self.rows = rows
        self.cols = cols
        self.min_value = min_value
        self.max_value = max_value

    def generate_matrix(self) -> list[list[int]]:
        matrix = []
        for _ in range(self.rows):
            row = [
                random.randint(self.min_value, self.max_value) for _ in range(self.cols)
            ]
            matrix.append(row)
        return matrix

    def __str__(self) -> str:
        matrix = self.generate_matrix()
        return "Сгенерированная матрица:\n" + "\n".join(str(row) for row in matrix)
