from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

def only_letters(value):
    if not value.isalpha():
        raise ValidationError("Fruit name should contain only letters!")


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            only_letters,
        ],
    )

    image_url = models.URLField()

    description = models.TextField()

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
