# Generated by Django 3.1.6 on 2021-08-09 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carolslist', '0006_auto_20210626_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credentials',
            old_name='StudentId',
            new_name='applicant',
        ),
        migrations.RenameField(
            model_name='grades',
            old_name='StudentId',
            new_name='applicant',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='StudentId',
            new_name='applicant',
        ),
        migrations.RenameField(
            model_name='typesofscholarship',
            old_name='nPrecincts',
            new_name='applicant',
        ),
    ]