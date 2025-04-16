from django.contrib import admin
from .models import Produit,Tag

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom','prix']
    list_filter = ['prix']
    search_fields = ['nom']



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['nom']