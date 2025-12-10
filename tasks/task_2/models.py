#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataclasses import dataclass, field

from exceptions import InvalidGradeError


@dataclass(frozen=True)
class Student:
    name: str
    group: int
    grades: list[int]

    def has_failing_grades(self) -> bool:
        return 2 in self.grades


@dataclass
class Staff:
    students: list[Student] = field(default_factory=lambda: [])

    def add(self, name: str, group: int, grades: str) -> None:

        try:
            grades_list = list(map(int, grades.split()))
            if len(grades_list) != 5:
                raise InvalidGradeError(grades, "Оценок должно быть ровно 5")
            for grade in grades_list:
                if grade < 2 or grade > 5:
                    raise InvalidGradeError(
                        grades, "Оценки должны быть в диапазоне от 2 до 5"
                    )
        except ValueError:
            raise InvalidGradeError(grades, "Оценки должны быть целыми числами")

        self.students.append(Student(name=name, group=group, grades=grades_list))
        self.students.sort(key=lambda student: student.name)

    def __str__(self) -> str:
        if not self.students:
            return "Список студентов пуст."

        line = f"+-{'-' * 4}-+-{'-' * 30}-+-{'-' * 20}-+-{'-' * 20}-+"
        header = f"| {'№':^4} | {'Ф.И.О':^30} | {'Группа':^20} | {'Оценки':^20} |"

        rows = [
            f"| {idx:>4} | {student.name:<30} | {student.group:>20} "
            f"| {' '.join(map(str, student.grades)):<20} |"
            for idx, student in enumerate(self.students, 1)
        ]

        return "\n".join([line, header, line, *rows, line])

    def select(self) -> list[Student]:
        return [student for student in self.students if student.has_failing_grades()]
