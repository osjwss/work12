from django.db import models

# Create your models here.

class Book(models.Model):
    genre = models.CharField(max_leght=100)
    year = models.IntegerField()
    price = models.IntegerField()
    author = models.ForeginKey('Author', on_delete=models.CASCADE)


class Author(models.Model):
    name = models.CharField(max_leght=100)
    country = models.CharField(max_leght=100)