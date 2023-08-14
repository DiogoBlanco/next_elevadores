from django.forms import ModelForm, DateInput
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'start_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy'}
            ),
            'expiration_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy'}
            ),
            'renewal_date': DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy'}
            ),
        }
