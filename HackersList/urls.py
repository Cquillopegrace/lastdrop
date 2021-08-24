"""HackersList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from carolslist import views
from django.conf.urls import url

from django.contrib import admin

urlpatterns = [  
    url('admin', admin.site.urls),    
    url(r'^$', views.Homerun, name='Homerun'),    
    url(r'^Home$', views.Home, name='Home'),
    url(r'^require$', views.require, name='require'),
    url(r'^Offered$', views.Offered, name='Offered'),
    url(r'^adminlogin$', views.adminlogin, name='adminlogin'),
    url(r'^List$', views.List, name='List'),
    url(r'^View$', views.View, name='View'),
    url(r'^AdminHome$', views.AdminHome, name='AdminHome'),
    url(r'^Homerun_Form$', views.Homerun_Form, name='Homerun_Form'), 
    url(r'^new$', views.new_applicant, name='new_applicant'),    
    url(r'^(\d+)/view_applicant$', views.view_applicant, name='view_applicant'),   
    url(r'^(\d+)/add_applicant$', views.add_applicant, name='add_applicant'),
    

    url(r'^adminaccount$', views.adminaccount, name='adminaccount'),  
    url(r'^applicant_list$', views.applicant_list, name='applicant_list'), 
    url(r'^(\d+)/applicant_view$', views.applicant_view, name='applicant_view'), 

    url(r'^applicant_page$', views.applicant_page, name='applicant_page'), 
    url(r'^admin_page$', views.admin_page, name='admin_page'), 

    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),]
    
    
 
# """HackersList URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from carolslist import views
# from django.conf.urls import url

# from django.contrib import admin

# urlpatterns = [    
#     url(r'^$', views.Homerun, name='Homerun'),    
#     url(r'^carolslist/new$', views.new_list, name='new_list'),
#     url(r'^carolslist/(\d+)/$', views.view_applicant, name='view_applicant'),
#     url(r'^carolslist/register/', views.registrationPage, name='register'),
#     url(r'^carolslist/login/', views.loginpage, name='login'),
#     url(r'^carolslist/Message$', views.Message, name='Message'),
#     url(r'^carolslist/Admin$', views.Admin, name='Admin'),
#     url(r'^carolslist/School1$', views.School1, name='School1'),
#     url(r'^carolslist/School2$', views.School2, name='School2'),
#     url(r'^carolslist/Register$', views.Register, name='Register'),
#     url(r'^carolslist/Contact$', views.Contact, name='Contact'),
#     url(r'^carolslist/Home$', views.Home, name='Home'),
#     url(r'^carolslist/Offered$', views.Offered, name='Offered'),
#     url(r'^carolslist/require$', views.require, name='require'),
#     url(r'^carolslist/Guide$', views.Guide, name='Guide'),
#     url(r'^carolslist/form$', views.Homerun_Form, name='Homerun_Form'),
#     url('admin/', admin.site.urls), 
    
#     url(r'^carolslist/edit/(?P<id>\d+)$', views.edit, name='edit'),
#     url(r'^carolslist/edit/update/(?P<id>\d+)$', views.update, name='update'),

#     url(r'^carolslist/delete/(?P<id>\d+)$', views.delete, name='delete'),
#     url(r'^carolslist/(\d+)/add_applicant$', views.add_applicant, name='add_applicant'),]
    
    
