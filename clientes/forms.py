from django import forms
from .models import ClientePF, ClientePJ


class ClientePFForm(forms.ModelForm):
    class Meta:
        model = ClientePF
        fields = '__all__'


class ClientePJForm(forms.ModelForm):
    class Meta:
        model = ClientePJ
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    TIPO_CLIENTE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    tipo_cliente = forms.ChoiceField(
        choices=TIPO_CLIENTE_CHOICES, label='Tipo de Cliente')
    nome = forms.CharField(max_length=30)
    sobrenome = forms.CharField(max_length=30)
    endereco = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=15)
    email = forms.EmailField()
    data_de_inicio = forms.DateTimeField()
    vigencia = forms.DateTimeField()
    data_de_renovacao = forms.DateTimeField()
    marca_dos_equipamentos = forms.ChoiceField(
        choices=[('Atlas', 'Atlas'),
                 ('Otis', 'Otis'),
                 ('Thyessen', 'Thyessen')])
    quantidade_de_elevadores = forms.IntegerField()
