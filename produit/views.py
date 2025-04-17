from django.shortcuts import render
from commande.models import Commande
from client.models import Client
from .models import Produit
# Create your views here.
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context = {'commandes':commandes,'clients':clients}
    return render(request,'produit/accueil.html',context)

def liste_produit(request):
    produits = Produit.objects.all()
    context = {'produits':produits}
    return render(request,'produit/index.html',context)