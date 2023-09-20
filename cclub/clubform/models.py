from django.core.exceptions import ValidationError
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Form(models.Model):
    def validate_name(self):
        if self != str:
            raise ValidationError("Некорректный ввод", code='odd', params={'name': self})

    name = models.CharField(max_length=30, validators=[validate_name])

    def validate_surname(self):
        if self != str:
            raise ValidationError("Некорректный ввод", code='odd', params={'surname': self})

    surname = models.CharField(max_length=30)

    def validate_age(self):
        if self < 18:
            raise ValidationError("Вам должно быть 18 или больше лет", code='odd', params={'age': self})

    age = models.IntegerField(validators=[validate_age])

    CHOICE = (('m', 'male'),
              ('f', 'female'),
              ('o', 'other'),
              ('nd', 'non defined'),
              ('ah', 'apache helicopter'))

    gender = models.CharField(max_length=100, choices=CHOICE)

    def validate_email(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if self != pattern:
            raise ValidationError("Некорректный ввод!", code='odd', params={'email': self})

    email = models.EmailField(validators=[validate_email])
    schedule_time = models.TimeField()
    phone_number = PhoneNumberField()
    username = models.CharField(max_length=100)
    favourite_game = models.CharField(max_length=100)

    CHOICES = (('YOUTUBE', 'Youtube'),
               ('INSTAGRAM', 'Instagram'),
               ('FRIENDS', 'Friends'),
               ('X', 'X'))

    place_of_notice = models.CharField(max_length=60, choices=CHOICES)
