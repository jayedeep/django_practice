from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Roles(Base):
    ROLES = [
        ('student',"Student"),
        ('teacher',"Teacher"),
    ]

    role_name = models.CharField(max_length=30,choices=ROLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.role_name


