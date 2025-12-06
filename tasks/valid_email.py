#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class InvalidEmailError(Exception):

    def __init__(
        self, email: str, message: str = "адрес не содержит '@' или домена"
    ) -> None:
        self.email = email
        self.message = message
        super(InvalidEmailError, self).__init__(self.message)

    def __str__(self) -> str:
        return f"{self.email} -> {self.message}"


class EmailValidator:

    def validate(self, email: str) -> str:

        if "@" not in email:
            raise InvalidEmailError(email)

        name, _, domain = email.partition("@")

        if "." not in domain:
            raise InvalidEmailError(email)

        if not name or not domain:
            raise InvalidEmailError(email)

        return f"Ваш {email} принят"
