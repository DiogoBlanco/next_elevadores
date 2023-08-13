from django.db import models


class Customer(models.Model):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name

    name = models.CharField(blank=False, null=False,
                            max_length=50, verbose_name='Nome:')
    address = models.CharField(
        blank=False, null=False, max_length=100, verbose_name='Endereço:')
    email = models.EmailField()
    phone = models.CharField(max_length=30, verbose_name='Telefone:')
    customer_since = models.DateTimeField(verbose_name='Cliente desde:')


class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=999)
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    renewal_date = models.DateTimeField()
    elevators_qty = models.IntegerField()
    elevators_brand = models.CharField(max_length=30)


class ModernizationContract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=999)
    installments_number = models.IntegerField()
    installments_value = models.DecimalField(decimal_places=2, max_digits=999)
    description = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
