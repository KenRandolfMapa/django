from django.shortcuts import render
from django.views.generic.list import ListView

from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth

from django.db.models import Count
from datetime import datetime


from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from studentorg.models import Organization,OrgMember, Student,Program, College
from studentorg.forms import OrganizationForm, StudentForm, ProgramForm, CollegeForm, OrgMemberForm
from django.urls import reverse_lazy
from django.utils.decorators import  method_decorator
from django.contrib.auth.decorators import login_required


from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q





from django.views.generic import View

from django.db import models

class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"


class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass


def StudentCountByProgram(request):
    # Fetching student counts per program
    program_counts = Student.objects.values('prog_name').annotate(count=Count('program')).order_by('-count')

    # Extracting labels (program names) and counts
    labels = [item['program__prog_name'] for item in program_counts]
    counts = [item['count'] for item in program_counts]

    data = {
        'labels': labels,
        'counts': counts,
    }
    return JsonResponse(data)


def OrganizationGraphData(request):
    # Your code to fetch organization graph data from the database or any other source
    # Example data for demonstration purposes
    labels = ['X', 'Y', 'Z']
    counts = [50, 70, 30]
    
    data = {
        'labels': labels,
        'counts': counts,
    }
    
    return JsonResponse(data)


def chart_students(request):
    program_counts = Program.objects.annotate(student_count=models.Count('student'))
    labels = [program.prog_name for program in program_counts]
    counts = [program.student_count for program in program_counts]
    return JsonResponse({'labels': labels, 'counts': counts})


def chart_org_members(request):
    org_counts = Organization.objects.annotate(member_count=models.Count('orgmember'))
    labels = [org.name for org in org_counts]
    counts = [org.member_count for org in org_counts]
    return JsonResponse({'labels': labels, 'counts': counts})


def chart_colleges(request):
    # Query the database to get data for the college pie chart
    # For example, let's say you want to count the number of students per college
    college_counts = College.objects.annotate(student_count=models.Count('program__student'))
    labels = [college.college_name for college in college_counts]
    counts = [college.student_count for college in college_counts]
    
    # Return the data as JSON response with a unique name
    return JsonResponse({'college_labels': labels, 'college_counts': counts})

#College
class CollegeDelView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = 'collelge_list'
    success_url = reverse_lazy('college-list')


class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeList(ListView):
    model = College
    template_name = 'college_list.html'
    success_url = reverse_lazy('college-list')
    paginate_by = 10

#program
class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = 'program_list'
    success_url = reverse_lazy('program-list')

class ProgramList(ListView):
    model = Program
    template_name = 'program_list.html'
    success_url = reverse_lazy('program-list')
    paginate_by = 10

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

#student
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = 'student_list'
    success_url = reverse_lazy('student-list')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('student-list')

class StudentList(ListView):
    model = Student
    template_name = 'student_list.html'
    success_url = reverse_lazy('student-list')
    paginate_by = 10

def forms_view(request):
    return render(request, 'forms.html', {})

#org member
class OrgMemberList(ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    context_object_name = 'orgmembers'
    paginate_by = 10


# Create a new OrgMember
class OrgMemberCreate(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember_list')


# Update an existing OrgMember
class OrgMemberUpdate(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember_list')


# Delete an OrgMember
class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_confirm_delete.html'
    success_url = reverse_lazy('orgmember_list')

# Organization
class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

@method_decorator([login_required], name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class organizationList(ListView):
    model=Organization
    context_object_name = 'organizations'
    template_name = 'org_list.html'
    paginate_by  =  10
    
    def get_qertyset(self, *rgs, **kwargs):
        qs = super(Organization, self).get_queryset(*rgs, **kwargs)
        if self.request.GET.get("q") !="None":
            query = self.request.GET.get("q")
            qs = qs.filter(Q(name__icontains=query)|Q(description__icontains=query))
        return qs

