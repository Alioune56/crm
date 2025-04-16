from django.shortcuts import render
from  django.http import HttpResponse


def list_commande(request):
    return render(request,'commande/list_commande.html')

def add(request):
    return HttpResponse("Nouveau Commande")