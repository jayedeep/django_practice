from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProxyUser(User):


    class Meta:
        proxy = True
        permissions = [
            ("can_add_student", "Can add student"),
            ("can_add_faculty", "Can add faculty"),
            # Add more custom permissions as needed
        ]