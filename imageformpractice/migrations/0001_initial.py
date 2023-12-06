# Generated by Django 4.2.4 on 2023-12-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='profile/')),
                ('file', models.FileField(upload_to='files/')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
