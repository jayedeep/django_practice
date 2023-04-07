from pyexpat import model
from random import choices

from django.db import models

# Create your models here.
class Student(models.Model):
    states = [('gujarat','Gujarat'),('rajsthan','Rajsthan'),('maharastra','Maharastra')]
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    state = models.CharField(max_length=100,choices=states)

    class Meta:
        verbose_name_plural = 'Students'
        db_table = 'student'
