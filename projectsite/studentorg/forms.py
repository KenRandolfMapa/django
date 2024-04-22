from django import forms
from .models import Organization, Student, Program, College

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = '__all__'
        
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model =  Student
        fields = '__all__'

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = '__all__'