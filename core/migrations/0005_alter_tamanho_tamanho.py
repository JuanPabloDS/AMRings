# Generated by Django 4.0.4 on 2022-07-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tamanho_anel_tamanho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamanho',
            name='tamanho',
            field=models.IntegerField(verbose_name='Tamanho'),
        ),
    ]
