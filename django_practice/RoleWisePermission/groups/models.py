from django.db import models
from django.contrib.auth.models import Group


# Create your models here.
class CustomGroup(Group):
    description = models.CharField(max_length=100,blank=True,null=True)

