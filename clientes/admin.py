from django.contrib import admin
from .models import Cliente, ClientePF, ClientePJ


class ClienteAdmin(admin.ModelAdmin):
    admin.site.register(Cliente)


class ClientePFAdmin(admin.ModelAdmin):
    admin.site.register(ClientePF)


class ClientePJAdmin(admin.ModelAdmin):
    admin.site.register(ClientePJ)
