from django.contrib import admin
from .models import Applicant, School, Grades, Credentials, TypesOfScholarship

admin.site.register(Applicant)
admin.site.register(School)
admin.site.register(Grades)
admin.site.register(Credentials)
admin.site.register(TypesOfScholarship)

# Register your models here.
