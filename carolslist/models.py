from django.db import models
# Create your models here.

class Applicant(models.Model):
	nFullName = models.TextField(default='')
	nAddress = models.TextField(default='')
	aage = models.IntegerField(default='0')
	nGenders = models.TextField(default='')
	acontumber = models.IntegerField(default='0')
	aemailAddress = models.TextField(default='')
	agname = models.TextField(default='')
	asoi = models.TextField(default='')
	nAIncome = models.IntegerField(default='0')
	ausername = models.TextField(default='')
	apassword = models.TextField(default='')
	sstatus = models.TextField(default='')

class School(models.Model):
	applicant = models.ForeignKey(Applicant, default=None, on_delete=models.CASCADE)
	NMSchool = models.TextField(default='')
	slevel = models.TextField(default='')
	nStudentId = models.TextField(default='')
	nGPA = models.IntegerField(default='0')
	sid  = models.ImageField(default='')
	sgwa = models.ImageField(default='')

class Admin(models.Model):
	adminu = models.TextField(default='')
	adminp = models.TextField(default='')














# from django.db import models
# # Create your models here.


# class Applicant(models.Model):
# 	n1StudentId = models.TextField(default='')
# 	nFullName = models.TextField(default='')
# 	nAddress = models.TextField(default='')
# 	nGenders = models.TextField(default='')
# 	nMoNames = models.TextField(default='')
# 	nOccupation1 = models.TextField(default='')
# 	nFaNames = models.TextField(default='')
# 	nOccupation2 = models.TextField(default='')
# 	nAIncome = models.IntegerField(default='0')
# 	NMSchool = models.TextField(default='')
# 	SAddress = models.TextField(default='')
# 	YSection = models.TextField(default='')
# 	n1GPA = models.IntegerField(default=1)
# 	nStudentId = models.ImageField(default='')
# 	nGPA = models.ImageField(default='')
# 	class meta:
# 		db_table = "Addapplicant"

# class School(models.Model):
# 	applicant = models.ForeignKey(Applicant, default =None, on_delete = models.CASCADE)
# 	NMSchool = models.TextField(default='')
# 	SAddress = models.TextField(default='')
# 	YSection = models.TextField(default='')
# 	class meta:
# 		db_table = "Addschool"

# class Grades(models.Model):
# 	applicant = models.OneToOneField(Applicant, default =None, on_delete = models.CASCADE)
# 	nGPA = models.TextField(default='')
# 	class meta:
# 		db_table = "grades"

# class Credentials(models.Model):
# 	applicant = models.ForeignKey(Applicant, default =None, on_delete = models.CASCADE)
# 	nAwards = models.TextField(default='')
# 	nCerts = models.TextField(default='')
# 	class meta:
# 		db_table = "credentials"

# class TypesOfScholarship(models.Model):
# 	applicant = models.ForeignKey(Applicant, default =None, on_delete = models.CASCADE)
# 	ApScholar = models.TextField(default='')
# 	class meta:
# 		db_table = "typeofscholarship"