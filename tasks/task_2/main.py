#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import sys

from exceptions import InvalidGradeError, UnknownCommandError
from models import Staff
from storage import StudentStorage


def show_help():
    help_text = """
    Список команд:

    add     - добавить студента;
    list    - вывести весь список студентов;
    select  - выполнить выборку по критерию (студенты с оценкой 2);
    save    - сохранить данные в XML файл;
    load    - загрузить данные из XML файла;
    help    - вывести справку;
    exit    - завершить программу.
    """
    print(help_text)


def main():
    logging.basicConfig(
        filename="student.log",
        level=logging.INFO,
        encoding="utf-8",
    )

    staff = Staff()

    try:
        students = StudentStorage.load("data.xml")
        staff.students = students
        staff.students.sort(key=lambda student: student.name)
        logging.info("Загружены данные из файла data.xml")
        print("Данные из файла data.xml успешно загружены.")
    except FileNotFoundError:
        logging.info("Файл data.xml не найден, начинаем с пустой базы")
    except Exception as e:
        logging.error(f"Ошибка при загрузке данных: {e}")
        print(f"Ошибка при загрузке данных: {e}")

    print("Программа для учета студентов")
    print("Введите 'help' для просмотра списка команд")

    while True:
        try:
            command = input(">>> ").lower()
            logging.info(f"Введена команда: {command}")

            if command == "exit":
                save_choice = (
                    input("Сохранить данные перед выходом? (y/n): ").strip().lower()
                )
                if save_choice == "y":
                    StudentStorage.save(staff.students, "students.xml")
                    logging.info("Данные сохранены перед выходом")
                    print("Данные сохранены в файл students.xml")

                print("Завершение работы программы...")
                logging.info("Программа завершена")
                break

            elif command == "add":
                name = input("Ф.И.О студента: ").strip()
                group = input("Номер группы: ").strip()
                print("Введите 5 оценок через пробел (например: 5 4 3 5 4):")
                grades = input("Оценки: ").strip()

                try:
                    staff.add(name, group, grades)
                    logging.info(
                        f"Добавлен студент: {name}, группа: {group}, оценки: {grades}"
                    )
                    print(f"Студент {name} успешно добавлен!")
                except InvalidGradeError as e:
                    logging.error(f"Ошибка при добавлении студента: {e}")
                    print(f"Ошибка: {e}")

            elif command == "list":
                print(staff)
                logging.info("Выведен полный список студентов")

            elif command == "select":
                selected = staff.select()
                if selected:
                    print("\nСтуденты с неудовлетворительными оценками (2):")
                    print("=" * 60)
                    for idx, student in enumerate(selected, 1):
                        print(
                            f"{idx:>3}. {student.name}, группа: {student.group}, "
                            f"оценки: {student.grades}"
                        )
                    print("=" * 60)
                    logging.info(f"Найдено {len(selected)} студентов с оценкой 2")
                else:
                    print("Студентов с неудовлетворительными оценками (2) не найдено.")
                    logging.info("Не найдено студентов с оценкой 2")

            elif command.startswith("save"):
                parts = command.split(maxsplit=1)
                if len(parts) > 1:
                    filename = parts[1]
                else:
                    filename = "students.xml"
                StudentStorage.save(staff.students, filename)
                logging.info(f"Сохранены данные в файл {filename}")
                print(f"Данные сохранены в файл {filename}")

            elif command.startswith("load"):
                parts = command.split(maxsplit=1)
                if len(parts) > 1:
                    filename = parts[1]
                else:
                    filename = "students.xml"
                try:
                    students = StudentStorage.load(filename)
                    staff.students = students
                    staff.students.sort(key=lambda student: student.name)
                    logging.info(f"Загружены данные из файла {filename}")
                    print(f"Данные из файла {filename} успешно загружены:")
                    print(staff)
                except FileNotFoundError:
                    logging.error(f"Файл {filename} не найден")
                    print(f"Файл {filename} не найден.")
                except Exception as e:
                    logging.error(f"Ошибка при загрузке из файла {filename}: {e}")
                    print(f"Ошибка при загрузке файла: {e}")
            elif command == "help":
                show_help()
                logging.info("Выведена справка по командам")

            else:
                raise UnknownCommandError(command)

        except UnknownCommandError as e:
            logging.error(f"Неизвестная команда: {command}")
            print(f"Ошибка: {e}")
            print("Введите 'help' для просмотра списка команд")

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            logging.warning("Программа прервана пользователем")
            break

        except Exception as e:
            logging.error(f"Неожиданная ошибка: {e}")
            print(f"Произошла ошибка: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
