from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(Base):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.DateField()

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        ordering = ['name']
        db_table = 'students'
        unique_together = ['name', 'email']


