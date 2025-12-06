#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from valid_email import EmailValidator, InvalidEmailError


def main():
    validator = EmailValidator()

    email = input("Введите email: ")

    try:
        print(validator.validate(email))
    except InvalidEmailError as e:
        print(e)


if __name__ == "__main__":
    main()
