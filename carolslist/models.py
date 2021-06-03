from django.db import models
# Create your models here.


class Applicant(models.Model):
	nStudentId = models.CharField(default='', max_length = 12)
	nFullName = models.TextField(default='')
	nAddress = models.TextField(default='')
	nGenders = models.TextField(default='')
	#nDBirths = models.DateTimeField(default='')
	nMoNames = models.TextField(default='')
	nOccupation1 = models.TextField(default='')
	nFaNames = models.TextField(default='')
	nOccupation2 = models.TextField(default='')
	nAIncome = models.CharField(default='', max_length = 6)
	class meta:
		db_table = "Addapplicant"

class School(models.Model):
	Napplicant = models.ForeignKey(Applicant, default =None, on_delete = models.CASCADE)
	NMSchool = models.TextField(default='')
	SAddress = models.TextField(default='')
	YSection = models.TextField(default='')
	class meta:
		db_table = "Addschool"

#class Grades(models.Model):
	#StudentId = models.OneToOneField(Applicant, default =None, on_delete = models.CASCADE)
	#nGPA = models.Charfield(default='')
	#class meta:
		#db_table = "grades"

#class Credentials(models.Model):
	#StudentId = models.ForeignKey(Applicant, default =None, on_delete = models.CASCADE)
	#nAwards = models.Textfield(default='')
	#nCerts = models.Textfield(default='')
	#class meta:
		#db_table = "credentials"

#class TypesOfScholarship(models.Model):
	#nPrecincts = models.OneToOneField(Applicant, default =None, on_delete = models.CASCADE)
	#ApScholar = models.Textfield(default='')
	#class meta:
		#db_table = "typeofscholarship"