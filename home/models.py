from django.db import models


class Customer(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    contract_types = (
        ('Manutenção', 'Manutenção'),
        ('Modernização', 'Modernização'),
    )
    first_name = models.CharField(max_length=30, verbose_name='Nome')
    last_name = models.CharField(max_length=30, verbose_name='Sobrenome')
    address = models.CharField(max_length=50, verbose_name='Endereço')
    city = models.CharField(max_length=30, null=True, verbose_name='Cidade')
    state = models.CharField(max_length=30, verbose_name='Estado')
    phone = models.CharField(max_length=14, verbose_name='Telefone')
    email = models.EmailField()
    contract = models.CharField(
        max_length=12, choices=contract_types, verbose_name='Tipo de Contrato')
    price = models.DecimalField(
        decimal_places=2, max_digits=999, verbose_name='Valor do Contrato/Mês')
    start_date = models.DateTimeField(verbose_name='Data de Início')
    expiration_date = models.DateTimeField(
        verbose_name='Data de Término do Contrato')
    renewal_date = models.DateTimeField(
        verbose_name='Data de Renovação', null=True, blank=True)
    elevators_qty = models.IntegerField(
        verbose_name='Quantidade de Elevadores')
    elevators_brand = models.CharField(
        max_length=30, verbose_name='Marca dos Elevadores')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
