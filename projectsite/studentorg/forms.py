from django import forms
from .models import Organization, Student

class StudentForm(forms.ModelForm):
    class Meta:
        model =  Student
        fields = '__all__'
        
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
