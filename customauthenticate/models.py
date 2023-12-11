from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from .manager import CustomUserManager



class Code(models.Model):
    code = models.CharField(max_length=6,blank=True,null=True)
    user = models.ForeignKey('CustomUser',on_delete=models.CASCADE)


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=100,null=True,blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

