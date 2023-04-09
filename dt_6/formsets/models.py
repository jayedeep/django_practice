from django.db import models

# Create your models here.
from django.db import models
from django.forms import formset_factory

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)