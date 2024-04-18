from django.shortcuts import render
from django.views.generic.list import ListView


from django.views.generic.edit  import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from django.utils.decorators import  method_decorator
from django.contrib.auth.decorators import login_required


from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

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


def forms_view(request):
    return render(request, 'forms.html', {})