
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from carolslist.models import Applicant, School, Grades, Credentials, TypesOfScholarship


def Homerun(request):
    return render(request, 'keps.html')

def Home(request):
    return render(request, 'keps.html')

def Offered(request):
    return render(request, 'scholarship.html')

def Form(request):
    return render(request, 'form.html')

def Homerun_Form(request):
    applicants = Applicant.objects.all()
    return render(request, 'form.html',{'applicants' : applicants})
    

def view_applicant(request, applicant_id):
    applicant_ = Applicant.objects.get(id=applicant_id)
    return render(request, 'school.html', {'applicant_': applicant_})

# def next_list(request, applicant_id):
#     applicant_ = Applicant.objects.get(id=applicant_id)
#     return render(request, 'school.html', {'applicant_': applicant_})

def new_list(request):
    applicants_ = Applicant.objects.create(nStudentId=request.POST['StudentID'],nFullName=request.POST['CompleteName'],nAddress=request.POST['Address'],nGenders=request.POST['Gender'],nMoNames=request.POST['MothersName'],nOccupation1=request.POST['MOccupation'],nFaNames=request.POST['FathersName'],nOccupation2=request.POST['FAOccupation'], nAIncome=request.POST['Annual Income'],)
    return redirect(f'/carolslist/{applicants_.id}/')

def add_applicant(request):
    applicant_ = Applicant.objects.create()
    School.objects.create(NMSchool=request.POST['School'],SAddress=request.POST['SAddress'],YSection=request.POST['YrSection'], applicant=applicant_)
    return redirect(f'/carolslist/{applicant_.id}/')

#def add_applicant(request, list_id):
    #list_ = List.objects.get(id=list_id)
    #Applicant.objects.create( NMSchool=request.POST['School'],SAddress =request.POST['SAddress'],YSection=request.POST['YSec.'],StudentId=request.POST['StudId'],nGPA=request.POST['GPA'],nAwards=request.POST['Award'],nCerts=request.POST['Certs'],ApScholar=request.POST['Scholar'], list=list_)
    #return redirect(f'/carolslist/{list_.id}/')


#def dataManipulation(request):
    #applicants = Applicant(nStudentId='StudId',nStatus='applicante', nPrecincts='0415', nFNames='Carol', nMNames='Bumotad', nLNames='Quillope', nAddress='Bacoor City', nGenders='Female', nDBirths='March 03,1998', nAges='23', nCPNos='09543367134', nMoNames='Fe', nOccupation1='HouseWife', nFaNames='Jimmy', nOccupation2='Carpenter',  nAIncome='50000' )
    #applicants.save()

    #objects = Applicant.object.all()
    #result = 'Printing all Applicant model : <br> '
    #for x in objects:
        #res += nStudentId +'br'

    #ApplicantName = applicants.object.get (id= '23')
    #res += 'Printing one Applicant entry <br>'
    #res += ApplicantName.nStatus

    #res += '<br> Deleting an Applicant entry <br> '
    #ApplicantName.delete()

    #applicants = Applicant(nStudentId='StudId',nStatus='applicante', nPrecincts='0415', nFNames='Carol', nMNames='Bumotad', nLNames='Quillope', nAddress='Bacoor City', nGenders='Female', nDBirths='March 03,1998', nAges='23', nCPNos='09543367134', nMoNames='Fe', nOccupation1='HouseWife', nFaNames='Jimmy', nOccupation2='Carpenter',  nAIncome='50000' )
    #applicants.save()
    #res += 'Updating Applicant entry <br>'

    #applicants = Applicant.object.get(nStudentId='StudId')
    #applicants = nStatus ='applicante'
    #applicants = nPrecincts ='0415'
    #applicants = nFNames='Carol'
    #applicants = nMNames='Bumotad'
    #applicants = nLNames='Quillope'
    #applicants = nAddress='Bacoor City'
    #applicants = nGenders='Female'
    #applicants = nDBirths='March 03,1998'
    #applicants = nAges='23'
    #applicants = nCPNos='09543367134'
    #applicants = nMoNames='Fe'
    #applicants = nOccupation1='HouseWife'
    #applicants = nFaNames='Jimmy'
    #applicants = nOccupation2='Carpenter'
    #applicants = nAIncome='50000'
    #applicants.save()
    #res += " "

    #qs = Applicant.objects.filter(nStudentId='StudId')
    #res += "Found : %s result <br>  " %len(qs)

    #qs = Applicant.object.order_by('nStudentId')
    #for x in qs:
        #res =+ x.nStudentId + x.nStatus + x.nPrecincts + x.nFNames + x.nMNames + x.nLNames + x.nAddress + x.nGenders + x.nDBirths + x.nAges + x.nCPNos + x.nMoNames + x.nOccupation1 + x.nFaNames + x.nOccupation2 + x.nAIncome = '<br'



 




