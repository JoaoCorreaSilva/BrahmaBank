from .models import *
from rest_framework import serializers


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ['numero', 'usuario', 'agencia', 'tipo', 'saldo', 'limite_cartao']

class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ['id', 'conta', 'numero', 'validade', 'bandeira', 'cvv']


class TransacaoSerializer(serializers.ModelSerializer):

    destinatario = serializers.IntegerField()
    quantia = serializers.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        model = Conta
        fields = ['conta', 'destinatario', 'quantia']


class TransacaoCartaoSerializer(serializers.ModelSerializer):

    quantia = serializers.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        model = Cartao
        fields = ['id', 'quantia']


class EmprestimoSerializer(serializers.ModelSerializer):

    salario = serializers.DecimalField(decimal_places=2, max_digits=7)

    class Meta:
        model = Emprestimo
        fields = ['id', 'conta', 'quantia', 'aprovado', 'salario']
        read_only_fields = ['id', 'aprovado', 'salario']


class FaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fatura
        fields = ['conta', 'tipo', 'valor', 'saldo']
