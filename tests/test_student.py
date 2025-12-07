#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest

from tasks.task_2.models import InvalidGradeError, Staff, Student


def test_add_student_valid():
    staff = Staff()
    staff.add("Ivanov Ivan", 101, "5 4 3 4 5")
    assert len(staff.students) == 1
    student = staff.students[0]
    assert student.name == "Ivanov Ivan"
    assert student.group == 101
    assert student.grades == [5, 4, 3, 4, 5]


def test_add_student_invalid_number_of_grades():
    staff = Staff()
    with pytest.raises(InvalidGradeError) as excinfo:
        staff.add("Petrov Petr", 102, "5 4 3 4")
    assert "Оценок должно быть ровно 5" in str(excinfo.value)


def test_add_student_invalid_grade_value():
    staff = Staff()
    with pytest.raises(InvalidGradeError) as excinfo:
        staff.add("Sidorov Sidr", 103, "5 4 3 1 5")
    assert "Оценки должны быть в диапазоне от 2 до 5" in str(excinfo.value)


def test_add_student_non_integer_grades():
    staff = Staff()
    with pytest.raises(InvalidGradeError) as excinfo:
        staff.add("Kuznetsov Kuz", 104, "5 4 3 A 5")
    assert "Оценки должны быть целыми числами" in str(excinfo.value)


def test_has_failing_grades():
    student1 = Student("Ivanov Ivan", 101, [5, 4, 3, 2, 5])
    student2 = Student("Petrov Petr", 102, [5, 4, 3, 3, 5])
    assert student1.has_failing_grades() is True
    assert student2.has_failing_grades() is False


def test_select_failing_students():
    staff = Staff()
    staff.add("Ivanov Ivan", 101, "5 4 3 2 5")
    staff.add("Petrov Petr", 102, "5 4 3 3 5")
    failing = staff.select()
    assert len(failing) == 1
    assert failing[0].name == "Ivanov Ivan"


def test_str_empty_staff():
    staff = Staff()
    output = str(staff)
    assert "Список студентов пуст." in output


def test_str_with_students():
    staff = Staff()
    staff.add("Ivanov Ivan", 101, "5 4 3 2 5")
    staff.add("Petrov Petr", 102, "5 4 3 3 5")
    output = str(staff)
    assert "Ivanov Ivan" in output
    assert "Petrov Petr" in output
    lines = output.splitlines()
    assert any("1 | Ivanov Ivan" in line for line in lines)
    assert any("2 | Petrov Petr" in line for line in lines)
