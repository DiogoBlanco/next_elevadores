from django.db import models
from clientes.models import Cliente


class TipoContrato(models.Model):
    nome = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.nome


class ContratoAnual(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    valor = models.PositiveIntegerField()
    vigencia = models.DateField(verbose_name='Vigência')
    data_de_renovacao = models.DateField(verbose_name='Data de Renovação')
    mes_reajuste = models.DateField(verbose_name='Mês de Reajuste')
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)

    def __str__(self):
        return f'Contrato de {self.cliente.nome} {self.cliente.sobrenome}'

    class Meta:
        verbose_name = 'Contrato Anual'
        verbose_name_plural = 'Contratos Anuais'
