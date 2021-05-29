from django.db import models

# Create your models here.

class List(models.Model):
    pass


class Applicant(models.Model):
    nNames = models.TextField(default='')
    nSchools = models.TextField(default='')
    nPrecincts = models.TextField(default='')
    nMnames = models.TextField(default='')
    nSyyear = models.TextField(default='')
    nGPAs = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)