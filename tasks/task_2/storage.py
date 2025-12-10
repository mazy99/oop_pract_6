#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import xml.etree.ElementTree as ET

from models import Student


class StudentStorage:

    @staticmethod
    def load(filename: str = "students.xml") -> list[Student]:
        folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "xml_files")
        )
        path = os.path.join(folder, filename)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Файл {path} не найден.")

        tree = ET.parse(path)
        root = tree.getroot()

        students: list[Student] = []

        for student_element in root:
            name_elem = student_element.find("name")
            group_elem = student_element.find("group")
            grades_elem = student_element.find("grades")

            if name_elem is None or group_elem is None or grades_elem is None:
                raise ValueError("Некорректная структура XML")

            name = name_elem.text or ""
            group = int(group_elem.text or "0")
            grades_str = grades_elem.text or ""
            grades = list(map(int, grades_str.split()))

            students.append(Student(name=name, group=group, grades=grades))

        return students

    @staticmethod
    def save(students: list[Student], filename: str = "students.xml") -> None:

        folder = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", "xml_files")
        )
        os.makedirs(folder, exist_ok=True)

        path = os.path.join(folder, filename)

        root = ET.Element("students")

        for student in students:
            student_element = ET.SubElement(root, "student")

            ET.SubElement(student_element, "name").text = student.name
            ET.SubElement(student_element, "group").text = str(student.group)
            ET.SubElement(student_element, "grades").text = " ".join(
                map(str, student.grades)
            )

        tree = ET.ElementTree(root)
        ET.indent(tree, space="  ", level=0)

        with open(path, "wb") as fout:
            tree.write(fout, encoding="utf-8", xml_declaration=True)
