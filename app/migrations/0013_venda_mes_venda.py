# Generated by Django 3.2.5 on 2021-08-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_pontofuncionario_mes_ponto'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='mes_venda',
            field=models.IntegerField(null=True),
        ),
    ]
