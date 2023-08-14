from django.contrib import admin
from .models import Budget

# Register your models here.


class BudgetAdmin(admin.ModelAdmin):
    admin.site.register(Budget)
