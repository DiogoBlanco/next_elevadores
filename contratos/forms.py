from django import forms
from .models import ContratoAnual


class ContratoForm(forms.ModelForm):
    def __init__(self, *args):
        super().__init__(*args)
        self.fields['data_de_renovacao'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )

    class Meta:
        model = ContratoAnual
        fields = '__all__'
