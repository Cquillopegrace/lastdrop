# Generated by Django 3.1.6 on 2021-06-26 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carolslist', '0005_credentials_grades_typesofscholarship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='Napplicant',
            new_name='StudentId',
        ),
    ]
