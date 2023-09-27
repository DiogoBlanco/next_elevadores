from django import forms
from .models import ClientePF, ClientePJ


class ClientePFForm(forms.ModelForm):

    class Meta:
        model = ClientePF
        fields = ['nome', 'sobrenome', 'cpf', 'endereco',
                  'telefone', 'email', 'data_de_inicio',
                  'marca_dos_equipamentos', 'quantidade_de_elevadores']


class ClientePJForm(forms.ModelForm):

    class Meta:
        model = ClientePJ
        fields = ['nome', 'cnpj', 'razao_social', 'endereco',
                  'telefone', 'email', 'data_de_inicio',
                  'marca_dos_equipamentos', 'quantidade_de_elevadores']


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=30)
    endereco = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=15)
    email = forms.EmailField()
    data_de_inicio = forms.DateInput()
    vigencia = forms.DateInput()
    marca_dos_equipamentos = forms.ChoiceField(
        choices=[('Atlas', 'Atlas'),
                 ('Otis', 'Otis'),
                 ('Thyessen', 'Thyessen')])
    quantidade_de_elevadores = forms.IntegerField()
