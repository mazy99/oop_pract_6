#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pytest

from tasks.valid_email import EmailValidator, InvalidEmailError


@pytest.fixture
def validator():
    return EmailValidator()


def test_valid_email(validator):
    email = "user@example.com"
    assert validator.validate(email) == f"Ваш {email} принят"


@pytest.mark.parametrize(
    "email",
    [
        "userexample.com",  # нет @
        "@example.com",  # нет имени
        "user@",  # нет домена
        "user@examplecom",  # нет точки в домене
        "@.",  # пустое имя и домен
    ],
)
def test_invalid_emails(validator, email):
    with pytest.raises(InvalidEmailError) as excinfo:
        validator.validate(email)
    assert email in str(excinfo.value)
    if "@" not in email or "." not in email:
        assert "адрес не содержит '@' или домена" in str(excinfo.value)
