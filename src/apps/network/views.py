from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from apps.network.models import Network

# Create your views here.
class NetWorkCreateView(generic.CreateView):
    model = Network
    fields = '__all__'
    template_name = 'network/create.html'
    success_url = reverse_lazy('apps.network:list-network')
 
class NetWorkListView(generic.ListView):
    model = Network
    template_name = 'network/list.html'
    context_object_name = 'networks'

    