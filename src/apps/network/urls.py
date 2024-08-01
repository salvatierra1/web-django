from django.urls import path
from apps.network.views import NetWorkCreateView, NetWorkListView

app_name = 'apps.network'

urlpatterns = [
    path('create/', NetWorkCreateView.as_view(), name='create-network'),
    path('list/', NetWorkListView.as_view(), name='list-network'),
]