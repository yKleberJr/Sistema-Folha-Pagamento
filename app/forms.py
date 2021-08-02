from project.settings import DATE_INPUT_FORMATS
from django.db import models
from django.db.models import fields
from app.models import Funcionario, PontoFuncionario, Venda
from django.forms import ModelForm


# Create the form class.
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'nome', 'endereco', 'tipo', 'salario', 'sindicato','taxa_sindicato',
            'forma_pagamento', 'comissao', 'data_pagamento'
        ]


class PontoForm(ModelForm):
    class Meta:
        model = PontoFuncionario
        fields = ['hora_entrada', 'hora_saida', 'data_ponto']


class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['nome_item', 'descricao_item', 'data_venda', 'valor_venda']
