from django.db import models
from home.models import Customer

# Create your models here.


class Budget(models.Model):
    class Meta:
        verbose_name = 'Orçamento'
        verbose_name_plural = 'Orçamentos'
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    description = models.TextField(
        max_length=1000, verbose_name='Descrição')
    deadline = models.CharField(
        max_length=30, verbose_name='Prazo de execução')
    value = models.DecimalField(
        decimal_places=2, max_digits=999, verbose_name='Valor')
    parcels = models.PositiveIntegerField(
        null=True, blank=True, verbose_name='Parcelas')
    parcels_value = models.CharField(
        max_length=30, verbose_name='Valor das Parcelas')
