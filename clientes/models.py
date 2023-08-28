from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    sobrenome = models.CharField(max_length=30, verbose_name='Sobrenome')
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField()
    data_de_inicio = models.DateField(verbose_name='Data de Início')
    vigencia = models.DateField(verbose_name='Vigência')
    data_de_renovacao = models.DateField(verbose_name='Data de Renovação')
    marca_dos_equipamentos = models.CharField(
        choices=[('Atlas', 'Atlas'), ('Otis', 'Otis'),
                 ('Thyessen', 'Thyessen')], max_length=8)
    quantidade_de_elevadores = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

        def __str__(self):
            return self.nome + ' ' + self.sobrenome


class ClientePF(Cliente):
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')

    class Meta:
        verbose_name = 'Cliente CPF'
        verbose_name_plural = 'Clientes CPF'

    def __str__(self):
        return self.nome + ' ' + self.sobrenome


class ClientePJ(Cliente):
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    razao_social = models.CharField(
        max_length=100, verbose_name='Razão Social')

    class Meta:
        verbose_name = 'Cliente CNPJ'
        verbose_name_plural = 'Clientes CNPJ'

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
