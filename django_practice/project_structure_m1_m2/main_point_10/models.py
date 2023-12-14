from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=30)

class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,null=True)
