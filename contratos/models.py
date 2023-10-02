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
    vigencia = models.CharField(
        choices=[('12 meses', '12 meses'), ('24 meses', '24 meses'),
                 ('36 meses', '36 meses'), ('48 meses', '48 meses')],
        max_length=8, null=True)
    data_de_renovacao = models.DateField(verbose_name='Data de Renovação')
    mes_reajuste = models.CharField(
        choices=[
            ('Janeiro', 'Janeiro'), ('Fevereiro', 'Fevereiro'), ('Março', 'Março'),
            ('Abril', 'Abril'), ('Maio', 'Maio'), ('Junho', 'Junho'),
            ('Julho', 'Julho'), ('Agosto', 'Agosto'), ('Setembro', 'Setembro'),
            ('Outubro', 'Outubro'), ('Novembro',
                                     'Novembro'), ('Dezembro', 'Dezembro')
        ],
        max_length=9
    )
    tipo_contrato = models.ForeignKey(TipoContrato, on_delete=models.CASCADE)
    marca_dos_elevadores = models.CharField(
        choices=[
            ('Atlas Schindler', 'Atlas Schindler'), ('Otis', 'Otis'),
            ('Hyundai', 'Hyundai'), ('Thyessen', 'Thyessen'),
            ('Villarta', 'Villarta')
        ],
        max_length=15
    )
    quantidade_de_elevadores = models.PositiveIntegerField()
    modelo_dos_elevadores = models.CharField(max_length=99)
    observacoes = models.TextField(max_length=999)

    def __str__(self):
        return f'Contrato de {self.cliente.nome} {self.cliente.sobrenome}'

    class Meta:
        verbose_name = 'Contrato Anual'
        verbose_name_plural = 'Contratos Anuais'
