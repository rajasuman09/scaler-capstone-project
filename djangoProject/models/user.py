from django.db import models


class User(models.Model):
    title = models.CharField(max_length=50, choices=[('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], default='Mr')
    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
