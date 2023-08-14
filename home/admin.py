from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    admin.site.register(Customer)
