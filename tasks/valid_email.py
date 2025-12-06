#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from exceptions import InvalidEmailError


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
