#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UnknownCommandError(Exception):

    def __init__(self, command: str, message: str = "Unknown command") -> None:
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(self.message)

    def __str__(self) -> str:
        return f"{self.command} -> {self.message}"


class InvalidGradeError(Exception):

    def __init__(self, grade: str, message: str = "Invalid grade") -> None:
        self.grade = grade
        self.message = message
        super(InvalidGradeError, self).__init__(self.message)

    def __str__(self) -> str:
        return f"{self.grade} -> {self.message}"
