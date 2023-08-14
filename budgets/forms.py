from django.forms import ModelForm, DateInput
from home.models import Customer
from .models import Budget


class BudgetForm(ModelForm):
    class Meta:
        model = Budget
        fields = '__all__'
        widgets = {
            'deadline': DateInput(
                attrs={'type': 'date', 'placeholder': 'dd-mm-yyyy'}
            ),
        }
