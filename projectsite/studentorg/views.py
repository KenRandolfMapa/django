from django.shortcuts import render
from django.views.generic.list import ListView


from django.views.generic.edit  import CreateView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')
    
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class organizationList(ListView):
    model=Organization
    context_object_name = 'organizations'
    template_name = 'org_list.html'
    paginate_by  = 5

def forms_view(request):
    return render(request, 'forms.html', {})