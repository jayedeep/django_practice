from django.shortcuts import reverse

from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Student(Base):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateTimeField()

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')
        unique_together = ('email', 'name')

    def get_absolute_url(self):
        return reverse('student_detail',kwargs={'pk':self.pk})

class Character(Base):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('Character Name'))

    class Meta:
        verbose_name = _('Character')
        verbose_name_plural = _('Characters')
        