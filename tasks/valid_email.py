#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
import os
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field

from exceptions import InvalidEmailError, UnknownCommandError


@dataclass(frozen=True)
class Contact:
    name: str
    email: str


@dataclass
class AddressBook:
    contacts: list[Contact] = field(default_factory=lambda: [])

    def add(self, name: str, email: str) -> None:
        if self.validate_email(email):
            self.contacts.append(Contact(name=name, email=email))
        self.contacts.sort(key=lambda contact: contact.name)

    def __str__(self) -> str:
        table = []
        line = "+-{}-+-{}-+-{}-+".format("-" * 4, "-" * 30, "-" * 40)
        table.append(line)
        table.append("| {:^4} | {:^30} | {:^40} |".format("№", "Имя", "Email"))
        table.append(line)

        for idx, contact in enumerate(self.contacts, 1):
            table.append(
                "| {:^4} | {:<30} | {:<40} |".format(idx, contact.name, contact.email)
            )
        table.append(line)

        return "\n".join(table)

    def select_domain(self, domain: str) -> list[Contact]:
        results = []
        for contact in self.contacts:
            if contact.email.endswith("@" + domain):
                results.append(contact)
        if not results:
            print(f"записей с доменом {domain} не найдено")
        return results

    def select_email(self, email: str) -> list[Contact]:
        results = []
        for contact in self.contacts:
            if contact.email == email:
                results.append(contact)
        if not results:
            print(f"записей с email {email} не найдено")
        return results

    def select_name(self, name: str) -> list[Contact]:
        results = []
        for contact in self.contacts:
            if contact.name == name:
                results.append(contact)
        if not results:
            print(f"записей с именем {name} не найдено")
        return results

    def load(self, filename: str) -> None:
        path = os.path.join("xml_files", filename)
        with open(path, "r", encoding="utf-8") as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.fromstring(xml, parser=parser)

        self.contacts = []
        for contact_element in tree:
            name, email = None, None
            for element in contact_element:
                if element.tag == "name":
                    name = element.text
                elif element.tag == "email":
                    email = element.text

                if name is not None and email is not None:
                    self.contacts.append(Contact(name=name, email=email))

    def save(self, filename: str = "addressbook.xml") -> None:
        folder = "xml_files"
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, filename)
        root = ET.Element("addressbook")

        for contact in self.contacts:
            contact_element = ET.SubElement(root, "contact")

            name_element = ET.SubElement(contact_element, "name")
            name_element.text = contact.name

            email_element = ET.SubElement(contact_element, "email")
            email_element.text = contact.email

        tree = ET.ElementTree(root)
        with open(path, "wb") as fout:
            tree.write(fout, encoding="utf-8", xml_declaration=True)

    def validate_email(self, email: str) -> bool:

        if "@" not in email:
            raise InvalidEmailError(email)
        username, _, domain = email.partition("@")

        if "." not in domain:
            raise InvalidEmailError(email)

        if not username:
            raise InvalidEmailError(email)

        if "." not in domain:
            raise InvalidEmailError(email)

        return True


if __name__ == "__main__":
    logging.basicConfig(
        filename="emailbook.log",
        level=logging.INFO,
        encoding="utf-8",
    )

    book = AddressBook()

    while True:
        try:
            command = input(">>> ").lower()

            if command == "exit":
                break

            elif command == "add":
                name = input("Имя: ")
                email = input("Email: ")
                book.add(name, email)
                logging.info(f"Добавлен контакт: {name}, {email}")
                print(f"Контакт {name} успешно добавлен.")

            elif command == "list":
                print(book)

            elif command.startswith("select_domain "):
                parts = command.split(maxsplit=1)
                domain = parts[1]
                selected = book.select_domain(domain)
                if selected:
                    for idx, contact in enumerate(selected, 1):
                        print(
                            "{:>4}: {}".format(
                                idx,
                                contact.email,
                            )
                        )
                logging.info(f"Выборка email по домену {domain}")

            elif command.startswith("select_email "):
                parts = command.split(maxsplit=1)
                email = parts[1]
                selected = book.select_email(email)
                if selected:
                    for idx, contact in enumerate(selected, 1):
                        print(
                            "{:>4}: {}".format(
                                idx,
                                contact.email,
                            )
                        )
                logging.info(f"Выборка email {email}")

            elif command.startswith("select_name "):
                parts = command.split(maxsplit=1)
                name = parts[1]
                selected = book.select_name(name)
                if selected:
                    for idx, contact in enumerate(selected, 1):
                        print(
                            "{:>4}: {}".format(
                                idx,
                                contact.name,
                            )
                        )
                logging.info(f"Выборка по имени {name}")

            elif command.startswith("load "):
                parts = command.split(maxsplit=1)
                book.load(parts[1])
                logging.info(f"Загружены данные из {parts[1]}")
                print(f"Файл {parts[1]} успешно загружен:")
                print(book)

            elif command.startswith("save"):
                parts = command.split(maxsplit=1)
                if len(parts) == 1:
                    book.save()
                    logging.info("Сохранено в файл addressbook.xml (по умолчанию)")
                else:
                    book.save(parts[1])
                    logging.info(f"Сохранено в файл {parts[1]}")
            elif command == "help":
                print("Команды:\n")
                print("add - добавить контакт;")
                print("list - вывести список;")
                print("select_domain <домен> - выбрать email по домену;")
                print("select_email <email> - выбрать контакт по email;")
                print("select_name <имя> - выбрать контакт по имени;")
                print("load <файл> - загрузить XML;")
                print("save <файл> - сохранить XML;")
                print("help - справка;")
                print("exit - выход.")

            else:
                raise UnknownCommandError(command)

        except Exception as err:
            logging.error(err)
            print(err, file=sys.stderr)
