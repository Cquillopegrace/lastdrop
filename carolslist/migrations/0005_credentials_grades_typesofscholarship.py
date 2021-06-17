# Generated by Django 3.1.6 on 2021-06-16 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carolslist', '0004_remove_applicant_ndbirths'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesOfScholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApScholar', models.TextField(default='')),
                ('nPrecincts', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='carolslist.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nGPA', models.TextField(default='')),
                ('StudentId', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='carolslist.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nAwards', models.TextField(default='')),
                ('nCerts', models.TextField(default='')),
                ('StudentId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='carolslist.applicant')),
            ],
        ),
    ]