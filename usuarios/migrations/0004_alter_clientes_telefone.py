# Generated by Django 4.0.4 on 2022-07-08 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_clientes_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='telefone',
            field=models.CharField(max_length=12),
        ),
    ]
