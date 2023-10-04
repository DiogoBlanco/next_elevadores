from django.contrib import admin
from .models import Cliente, ClientePF, ClientePJ


class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'sobrenome', 'id', 'contratoanual']
    admin.site.register(Cliente)


class ClientePFAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'sobrenome', 'id', 'contratoanual']
    admin.site.register(ClientePF)


class ClientePJAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'sobrenome', 'id', 'contratoanual']
    admin.site.register(ClientePJ)
