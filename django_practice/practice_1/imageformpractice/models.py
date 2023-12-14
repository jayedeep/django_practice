from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/')
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=50)
    