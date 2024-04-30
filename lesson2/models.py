from django.db import models

# Create your models here.

class Book(models.Model):
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)