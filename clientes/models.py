from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_de_inicio = models.DateTimeField()
    vigencia = models.DateTimeField()
    data_de_renovacao = models.DateTimeField()
    marca_dos_equipamentos = models.CharField(
        choices=[('Atlas', 'Atlas'), ('Otis', 'Otis'),
                 ('Thyessen', 'Thyessen')], max_length=8)
    quantidade_de_elevadores = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        def __str__(self):
            return self.nome + '' + self.sobrenome


class ClientePF(Cliente):
    cpf = models.CharField(max_length=14, unique=True)


class ClientePJ(Cliente):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=100)
