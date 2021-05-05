
# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from carolslist.models import Item, List


def Homerun(request):
    items = Item.objects.all()
    return render(request, 'keps.html',{'items' : items})
    


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'form.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(nNames=request.POST['Name'],nSchools =request.POST['School'],nPrecincts=request.POST['Precinct'], list=list_)
    return redirect(f'/carolslist/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create( nMnames=request.POST['NxtName'],nSyyear =request.POST['Year'],nGPAs=request.POST['GPA'], list=list_)
    return redirect(f'/carolslist/{list_.id}/')
