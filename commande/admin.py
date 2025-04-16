from django.contrib import admin
from .models import Commande

@admin.register(Commande)
class Commande(admin.ModelAdmin):
    list_display = ['client','produit','status']
