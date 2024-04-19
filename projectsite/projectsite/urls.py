"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import HomePageView, organizationList,OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,StudentList,StudentUpdateView, StudentCreateView ,StudentDeleteView, CollegeList, OrgMemberList
from studentorg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='Home'),
    path('forms.html', views.forms_view, name='forms'),
    path('organization_list', organizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',  OrganizationUpdateView.as_view(), name="organization-update"),
    path('organization_list/<pk>/delete',  OrganizationDeleteView.as_view(), name="organization-delete"),
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    #student
    path('students_list', StudentList.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name = 'student-add'),
    path('student_list/<int:pk>/', StudentUpdateView.as_view(), name='student-edit'),
    path('student_list/<int:pk>/delete', StudentDeleteView.as_view(), name='student-del'),


    #College
    path("college", CollegeList.as_view(), name="college-list"),
    
    #Org member
    path('orgmember_list', OrgMemberList.as_view(), name= 'orgmember-list'),

]
