from django import forms
from .models import ClientePF, ClientePJ


class ClientePFForm(forms.ModelForm):
    def __init__(self, *args):
        super().__init__(*args)
        self.fields['data_de_inicio'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )
        self.fields['vigencia'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )
        self.fields['data_de_renovacao'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )

    class Meta:
        model = ClientePF
        fields = '__all__'


class ClientePJForm(forms.ModelForm):
    def __init__(self, *args):
        super().__init__(*args)
        self.fields['data_de_inicio'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )
        self.fields['vigencia'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )
        self.fields['data_de_renovacao'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date',
                'placeholder': 'dd-mm-yyyy',
            }
        )

    class Meta:
        model = ClientePJ
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=30)
    endereco = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=15)
    email = forms.EmailField()
    data_de_inicio = forms.DateInput()
    vigencia = forms.DateInput()
    data_de_renovacao = forms.DateInput()
    marca_dos_equipamentos = forms.ChoiceField(
        choices=[('Atlas', 'Atlas'),
                 ('Otis', 'Otis'),
                 ('Thyessen', 'Thyessen')])
    quantidade_de_elevadores = forms.IntegerField()
