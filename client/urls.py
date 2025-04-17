from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_clients,name= 'client')
]