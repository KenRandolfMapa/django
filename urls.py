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
from studentorg.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country
from studentorg.views import organizationList,OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView
from studentorg.views import StudentList,StudentUpdateView, StudentCreateView ,StudentDeleteView
from studentorg.views import ProgramList, ProgramCreateView,ProgramUpdateView, ProgramDeleteView
from studentorg.views import CollegeList,CollegeCreateView, CollegeUpdateView, CollegeDelView
from studentorg.views import OrgMemberList, OrgMemberCreate, OrgMemberUpdate,OrgMemberDeleteView
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

    #program
    path('program_list', ProgramList.as_view(), name ='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name = 'program-add'),
    path('program_list/<int:pk>/', ProgramCreateView.as_view(), name='program-edit'),
    path('program_list/<int:pk>/delete', ProgramDeleteView.as_view(), name='program-del'),


    #College
    path('college_list', CollegeList.as_view(), name='college-list'),
    path('college_list/add',  CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<int:pk>', CollegeUpdateView.as_view(), name = 'college-edit'),
    path('college_list/<int:pk>/delete', CollegeDelView.as_view(), name = 'college-del'),
    
    #Org member
    path('orgmember_list', OrgMemberList.as_view(), name= 'orgmember-list'),
    path('orgmembers/add/', OrgMemberCreate.as_view(), name='orgmember_add'),
    path('orgmembers/edit/<int:pk>/', OrgMemberUpdate.as_view(), name='orgmember_edit'),
    path('orgmembers/delete/<int:pk>/', OrgMemberDeleteView.as_view(), name='orgmember_delete'),

    #chartview
    path('dashboard_chart', ChartView.as_view(), name = 'dashboard-chart'),
    path('chart/', PieCountbySeverity, name = 'chart'),
    path('multilineChrt/', MultilineIncidentTop3Country, name = 'chart'),
]
