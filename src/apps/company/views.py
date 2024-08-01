from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from apps.company.models import Company


# Create your views here.
class CustomersCreateView(generic.CreateView):
    model= Company
    fields= '__all__'
    template_name = 'company/create.html'
    success_url = reverse_lazy('apps.customers:list')