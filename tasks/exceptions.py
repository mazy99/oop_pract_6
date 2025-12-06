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


class UnknownCommandError(Exception):

    def __init__(self, command: str, message: str = "Unknown command") -> None:
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(self.message)

    def __str__(self) -> str:
        return f"{self.command} -> {self.message}"
