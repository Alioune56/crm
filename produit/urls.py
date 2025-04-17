from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('liste', views.liste_produit,name='produit')
]