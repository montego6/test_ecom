from django.db import models
from abc import ABC

# Create your models here.
class 

class DataValidator:
    @staticmethod
    def validate(value):
        regex = r'^(\d{2}\.\d{2}\.\d{4})|()'