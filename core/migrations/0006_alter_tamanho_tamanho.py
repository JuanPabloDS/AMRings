# Generated by Django 4.0.4 on 2022-07-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_tamanho_tamanho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamanho',
            name='tamanho',
            field=models.CharField(max_length=2, verbose_name='Tamanho'),
        ),
    ]
