# Generated by Django 4.1.5 on 2023-03-15 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_alter_customuser_author_of'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='author_of',
        ),
    ]