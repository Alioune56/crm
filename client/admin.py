from django.contrib import admin
from .models import Client
@admin.register(Client)
class Client(admin.ModelAdmin):
    list_display = ['nom','telephone']
    list_filter = ['nom']
    search_fields = ['nom']
