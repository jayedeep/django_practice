# Generated by Django 4.2.4 on 2023-11-25 11:49

from django.db import migrations, models
import django.db.models.deletion
import datetime


def insert_my_initial_data(apps,schema_editor):
    Student = apps.get_model('firstthreetopics', 'Student')
    Character = apps.get_model('firstthreetopics', 'Character')

    student_names = [{'name':'elena','age':20,'char':'elena'},{'name':'stefan','age':200,'char':'vampire'},{'name':'damon','age':210,'char':'vampire brother'}]
    for student in student_names:
        new_student = Student(name=student.get('name'),email=student.get('name')+'@gmail.com',date_of_birth = datetime.datetime.now() - datetime.timedelta(days=student.get('age')*365))
        new_student.save()
        character = Character.objects.create(name=student.get('char'),student=new_student)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'unique_together': {('email', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, verbose_name='Character Name')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstthreetopics.student')),
            ],
            options={
                'verbose_name': 'Character',
                'verbose_name_plural': 'Characters',
            },
        ),
        migrations.RunPython(insert_my_initial_data)
    ]
