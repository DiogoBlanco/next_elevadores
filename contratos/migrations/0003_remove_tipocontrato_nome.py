# Generated by Django 4.2.4 on 2023-08-31 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0002_alter_contratoanual_mes_reajuste_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipocontrato',
            name='nome',
        ),
    ]