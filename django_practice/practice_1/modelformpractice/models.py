from django.db import models
from formpractice.models import Base
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Teacher(Base):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bod = models.DateField()

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
        ordering = ['name']
        db_table = 'teachers'
        unique_together = ['name', 'email']