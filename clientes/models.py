from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=30, verbose_name='Nome')
    sobrenome = models.CharField(max_length=30, verbose_name='Sobrenome')
    endereco = models.CharField(max_length=50, verbose_name='Endereço')
    numero = models.PositiveIntegerField(verbose_name='Número')
    cep = models.CharField(max_length=9)
    telefone = models.CharField(max_length=15, verbose_name='Telefone')
    email = models.EmailField()
    data_de_criacao = models.DateField(
        verbose_name='Data de Criação', auto_now_add=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class ClientePF(Cliente):
    cpf = models.CharField(max_length=14, unique=True, verbose_name='CPF')

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        verbose_name = 'Cliente CPF'
        verbose_name_plural = 'Clientes CPF'


class ClientePJ(Cliente):
    cnpj = models.CharField(max_length=18, unique=True, verbose_name='CNPJ')
    razao_social = models.CharField(
        max_length=100, verbose_name='Razão Social')

    def __str__(self):
        return self.nome + ' ' + self.sobrenome

    class Meta:
        verbose_name = 'Cliente CNPJ'
        verbose_name_plural = 'Clientes CNPJ'
