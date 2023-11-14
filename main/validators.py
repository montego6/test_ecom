from abc import ABC
import re


class Validator(ABC):
    @classmethod
    def validate(cls, value):
        return bool(re.match(cls.regex, value))


class DateValidator(Validator):
    type = "date"
    regex = r"^(\d{2}\.\d{2}\.\d{4})|(\d{4}-\d{2}-\d{2})$"


class PhoneValidator(Validator):
    type = "phone"
    regex = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"


class EmailValidator(Validator):
    type = "email"
    regex = r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$"


class TextValidator(Validator):
    type = "text"
    regex = r".*"


def get_data_type(value):
    validators = [DateValidator, PhoneValidator, EmailValidator, TextValidator]
    for validator in validators:
        if validator.validate(value):
            return validator.type
