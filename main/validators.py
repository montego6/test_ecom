from abc import ABC, abstractmethod
import re

# Create your models here.
class Validator(ABC):
    @abstractmethod
    def validate(value):
        pass


class DataValidator(Validator):
    @staticmethod
    def validate(value):
        regex = r'^(\d{2}\.\d{2}\.\d{4})|(\d{4}-\d{2}-\d{2})$'
        return bool(re.match(regex, value))
    

class PhoneValidator(Validator):
    @staticmethod
    def validate(value):
        regex = r'^+7 \d{3} \d{3} \d{2} \d{2}'
        return bool(re.match(regex, value))
    

class EmailValidator(Validator):
    @staticmethod
    def validate(value):
        regex = r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$'
        return bool(re.match(regex, value))