from django.shortcuts import render, redirect
from django.http import HttpResponse
from carolslist.models import Applicant, School , Admin 
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt


def Homerun(request):
    return render(request, 'keps.html')

def Home(request):
    return render(request, 'keps.html')

def Offered(request):
    return render(request, 'login.html')

def adminlogin(request):
    return render(request, 'userslogin.html')

def Message(request) :
    return render(request, 'results.html')

def List(request) :
    return render(request,'applicant_list.html')

def View(request) :
    return render(request,'applicant_view.html')

def AdminHome(request):
    return render(request, 'adminaccount.html')

def Homerun_Form(request):
    applicants = Applicant.objects.all()
    return render(request, 'form.html',{'applicants' : applicants})


def new_applicant(request):
    applicants_ = Applicant.objects.create(nFullName=request.POST['CompleteName'],nAddress=request.POST['Address'],aage=request.POST['Aage'],nGenders=request.POST['Gender'],acontumber =request.POST['Cnumber'],aemailAddress=request.POST['EmailAdd'],agname=request.POST['GName'],asoi=request.POST['Occupation'], nAIncome=request.POST['Annual Income'],ausername =request.POST['Usersname'],apassword=request.POST['Passwords'],sstatus=request.POST['stats'])
    return redirect(f'/{applicants_.id}/view_applicant') 

def view_applicant(request, applicant_id):
    applicant_ = Applicant.objects.get(id=applicant_id)
    return render(request, 'school.html', {'applicant': applicant_})


def add_applicant(request,applicant_id):
    applicant_ = Applicant.objects.get(id=applicant_id)
    School.objects.create(NMSchool=request.POST['School'],slevel=request.POST['GradeLevel'],nStudentId=request.POST['StudsId'],nGPA=request.POST['GPA'],sid =request.POST['img'],sgwa=request.POST['img1'],applicant=applicant_)
    return redirect(f'/{applicant_.id}/view_applicant')


def applicant_page(request): 
 if request.method == 'POST':
        if Applicant.objects.filter(ausername=request.POST['Usersname'], apassword=request.POST['Passwords']).exists():
            applicant_ = Applicant.objects.get(ausername=request.POST['Usersname'], apassword=request.POST['Passwords'])
            return redirect(f'/{applicant_.id}/view_applicant')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'Offered', context)


def adminaccount(request):
    admins = Admin.objects.all()
    return render(request, 'adminaccount.html', {'admins' : admins})

def applicant_list(request): 
   applicants = Applicant.objects.all() 
   return render(request, 'applicant_list.html',{'applicants' : applicants})

def applicant_view(request, applicant_id):   
   applicant_ = Applicant.objects.get(id=applicant_id)
   school = School.objects.all()
   return render(request, 'applicant_view.html', {'applicant': applicant_,'school' : school})    

def admin_page(request): 
 if request.method == 'POST':
        if Admin.objects.filter(adminu=request.POST['aadminu'], adminp=request.POST['aadminp']).exists():
            admin_ = Admin.objects.get(adminu=request.POST['aadminu'], adminp=request.POST['aadminp'])
            return redirect(f'/adminaccount')

        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)




def edit(request, id):
    applicants = Applicant.objects.get(id=id)
    context = {'applicants' : applicants}
    return render(request, 'crud.html', context)

def update(request, id):
    applicant= Applicant.objects.get(id=id)
    applicant.nFullName = request.POST['CompleteName']
    applicant.nAddress = request.POST['Address']
    applicant.aage = request.POST['Aage']
    applicant.nGenders = request.POST['Gender']
    applicant.acontumber = request.POST['Cnumber']
    applicant.aemailAddress = request.POST['EmailAdd']
    applicant.agname = request.POST['GName']
    applicant.asoi= request.POST['Occupation']
    applicant.nAIncome = request.POST['Annual Income']
    applicant.ausername = request.POST['Usersname']
    applicant.apassword = request.POST['Passwords']
    applicant.save()
    return redirect ('/applicant_list')

def delete(request, id):
    applicant = Applicant.objects.get(id=id)
    applicant.delete()
    return redirect ('/applicant_list')




# Create your views here.
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from carolslist.models import Applicant, School, Grades, Credentials, TypesOfScholarship
# from django.contrib.auth.forms import UserCreationForm
# from django.views.decorators.csrf import csrf_exempt


# def Homerun(request):
#     return render(request, 'keps.html')

# def Home(request):
#     return render(request, 'keps.html')

# def registrationPage(request):
#     form = UserCreationForm()
#     if form.is_valid():
#         form.save()

#     context ={'form':form}
#     return render (request, 'register.html', context)

# def loginpage(request):
#     context = {}
#     return render(request,'login.html', context)

# def Offered(request):
#     return render(request, 'login.html')

# def require(request):
#     return render(request, 'require.html')

# def Register(request) :
#     return render(request, 'register.html')

# def Guide(request) :
#     return render(request, 'keps.html')

# def Message(request) :
#     return render(request, 'results.html')

# def Admin(request) :
#     return render(request, 'admin.html')

# def School1(request) :
#     return render(request, 'school.html')

# def School2(request) :
#     return render(request, 'form.html')

# def Contact(request) :
#     return render(request, 'contact.html')


# def Homerun_Form(request):
#     applicants = Applicant.objects.all()
#     return render(request, 'form.html',{'applicants' : applicants})
    

# def view_applicant(request, applicant_id):
#     applicant_ = Applicant.objects.get(id=applicant_id)
#     return render(request, 'school.html', {'applicant': applicant_})


# def new_list(request):
#     applicants_ = Applicant.objects.create(n1StudentId=request.POST['StudentID'],nFullName=request.POST['CompleteName'],nAddress=request.POST['Address'],nGenders=request.POST['Gender'],nMoNames=request.POST['MothersName'],nOccupation1=request.POST['MOccupation'],nFaNames=request.POST['FathersName'],nOccupation2=request.POST['FAOccupation'], nAIncome=request.POST['Annual Income'],NMSchool=request.POST['School'],SAddress=request.POST['SAddress'],YSection=request.POST['YrSection'],n1GPA=request.POST['Grade'],nStudentId=request.POST['img'],nGPA=request.POST['img1'])
#     return redirect(f'/carolslist/{applicants_.id}/')

# def add_applicant(request,applicant_id):
#     applicant_ = Applicant.objects.get(id=applicant_id)
#     School.objects.create(NMSchool=request.POST['School'],SAddress=request.POST['SAddress'],YSection=request.POST['YrSection'],applicant=applicant_)
#     return redirect(f'/carolslist/{applicant_.id}/')


# def edit(request, id):
#     applicants = Applicant.objects.get(id=id)
#     context = {'applicants' : applicants}
#     return render(request, 'crud.html', context)

# def update(request, id):
#     applicant= Applicant.objects.get(id=id)
#     applicant.nStudentId = request.POST['StudentID']
#     applicant.nFullName = request.POST['CompleteName']
#     applicant.nAddress = request.POST['Address']
#     applicant.nGenders = request.POST['Gender']
#     applicant.nMoNames = request.POST['MothersName']
#     applicant.nOccupation1 = request.POST['MOccupation']
#     applicant.nFaNames = request.POST['FathersName']
#     applicant.nOccupation2= request.POST['FAOccupation']
#     applicant.nAIncome = request.POST['Annual Income']
#     applicant.save()
#     return redirect ('/carolslist/form')

# def delete(request, id):
#     applicant = Applicant.objects.get(id=id)
#     applicant.delete()
#     return redirect ('/carolslist/form')




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



 




