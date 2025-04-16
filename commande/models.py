from django.db import models
from client.models import Client
from produit.models import Produit
class Commande(models.Model):
    STATUS = (('en instance','en instance'),
              ('non livre','non livre'),
              ('livre','livre'))

    client = models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    produit = models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL)
    status = models.CharField(max_length=100,null=True,choices=STATUS)
    date_creation = models.DateTimeField(auto_now_add=True)
