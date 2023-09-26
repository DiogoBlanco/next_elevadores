from django.contrib import admin
from .models import ContratoAnual, TipoContrato


class ContratoAnualAdmin(admin.ModelAdmin):
    admin.site.register(ContratoAnual)


class TipoContratoAdmin(admin.ModelAdmin):
    admin.site.register(TipoContrato)
