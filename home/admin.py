from django.contrib import admin
from .models import Customer, Contract, ModernizationContract


class CustomerAdmin(admin.ModelAdmin):
    admin.site.register(Customer)


class ContractAdmin(admin.ModelAdmin):
    admin.site.register(Contract)


class ModernizationContractAdmin(admin.ModelAdmin):
    admin.site.register(ModernizationContract)
