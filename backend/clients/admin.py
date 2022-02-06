from pydoc import cli
from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'address', 'age', 'sexe')

# Register your models here.
admin.site.register(Client, ClientAdmin)