from django.db import models
import django.core.validators as validators
from .validators import validate_zipcode
from .utils import CoffeeType, Size, QuantityChoices

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.username


class UserDetails(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100,validators=[validators.MinLengthValidator(10)])
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10, validators=[validate_zipcode])

    def __str__(self):
        return self.username

class Coffee(models.Model):
    name = models.CharField(max_length=10, choices=CoffeeType.choices)
    size = models.CharField(max_length=1, choices=Size.choices)
    quantity = models.CharField(max_length=1, choices=QuantityChoices.choices)

    def __str__(self):
        return self.name