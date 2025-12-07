#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest

from tasks.matrix_generate import MatrixGenerator


@pytest.mark.parametrize(
    "rows, cols, min_val, max_val",
    [
        (3, 3, 0, 10),
        (5, 2, 1, 5),
        (1, 1, -10, 10),
    ],
)
def test_matrix_size_and_values(rows, cols, min_val, max_val):
    generator = MatrixGenerator(rows, cols, min_val, max_val)
    matrix = generator.generate_matrix()

    assert len(matrix) == rows
    for row in matrix:
        assert len(row) == cols
        for value in row:
            assert min_val <= value <= max_val


def test_str_output_contains_rows():
    generator = MatrixGenerator(2, 3, 0, 5)
    output = str(generator)
    assert "Сгенерированная матрица:" in output
    lines = output.split("\n")[1:]
    for line in lines:
        assert any(char.isdigit() for char in line)


def test_min_equals_max():
    # Если min_value == max_value, все элементы равны этому значению
    generator = MatrixGenerator(2, 2, 7, 7)
    matrix = generator.generate_matrix()
    for row in matrix:
        for value in row:
            assert value == 7
