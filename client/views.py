from django.shortcuts import render
from django.http import HttpResponse

def list_clients(request):
    return render(request,'client/list_client.html')
