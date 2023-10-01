from django import forms
from .models import ClientePF, ClientePJ, Cliente


class ClientePFForm(forms.ModelForm):

    class Meta:
        model = ClientePF
        fields = ['nome', 'sobrenome', 'cpf', 'endereco',
                  'numero', 'cep', 'telefone', 'email']


class ClientePJForm(forms.ModelForm):

    class Meta:
        model = ClientePJ
        fields = ['nome', 'cnpj', 'razao_social', 'endereco',
                  'numero', 'cep', 'telefone', 'email']


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=30)
    endereco = forms.CharField(max_length=50)
    numero = forms.NumberInput()
    cep = forms.CharField(max_length=9)
    telefone = forms.CharField(max_length=15)
    email = forms.EmailField()
