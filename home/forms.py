from django.forms import ModelForm
from .models import Contract, Customer, ModernizationContract


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
