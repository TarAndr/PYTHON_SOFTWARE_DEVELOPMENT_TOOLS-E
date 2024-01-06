# models.py

from django.db import models

class Human(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_birth = models.DateField()
    place_residence = models.CharField(max_length=255)

    def __str__(self):
        return f"{self. name} {self. surname} {self. date_birth} ({self. place_residence})"
