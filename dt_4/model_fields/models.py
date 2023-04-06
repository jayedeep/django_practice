from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        null=True,
        blank=True,
        default=None
    )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        null=True,
        blank=True,
        default=None,
    )
    tags = models.ManyToManyField('Tag', related_name='books',through='BooksTags')


class Tag(models.Model):
    name = models.CharField(max_length=50)

class BooksTags(models.Model):
    Book = models.ForeignKey(Book,on_delete=models.CASCADE)
    Tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    color = models.CharField(max_length=50)

# Check Database... to see data.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Students'
        db_table = 'student'
        unique_together = ('name','email','phone')