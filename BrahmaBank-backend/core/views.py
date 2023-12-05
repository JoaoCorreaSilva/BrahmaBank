from rest_framework import viewsets, status
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import random
from decimal import Decimal

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

    def create(self, request, *args, **kwargs):
        ultima_conta = Conta.objects.order_by('-numero').first()
        if ultima_conta:
            proxima = ultima_conta.numero + 1
        else:
            proxima = 1111

        tipo_conta = request.data.get('tipo')

        conta = Conta.objects.create(
            numero = proxima,
            agencia = 1,
            tipo = tipo_conta,
            saldo = 1500,
            limite_cartao = 1500
        )
        conta.usuario.add(self.request.user)

        serializer = ContaSerializer(conta)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

    def create(self, request, *args, **kwargs):
        range = 13
        conta = request.data.get('conta')
        cartao = Cartao.objects.create(
            conta = get_object_or_404(Conta, pk=conta),
            numero = random.randint(10 ** (range - 1), (10 ** range) - 1),
            validade = '2025-06-19',
            bandeira = 'Visa',
            cvv = random.randint(10 ** (3 - 1), (10 ** 3) - 1)
        )
        serializer = CartaoSerializer(cartao)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class TransacaoCartaoViewSet(viewsets.GenericViewSet):
    serializer_class = TransacaoCartaoSerializer

    def create(self, request): 
        cartao = get_object_or_404(Cartao, pk=request.data.get('id'))
        conta = cartao.conta
        quantia = Decimal(request.data.get('quantia'))

        if conta.limite_cartao >= quantia:
            conta.limite_cartao -= quantia
            conta.save()

            fatura_cartao = Fatura.objects.create(
                conta = conta,
                tipo = 'cartao',
                valor = quantia,
                saldo = conta.saldo
            )

            return Response({'Sucesso': 'Compra com cartão realizada com sucesso'}, status=status.HTTP_201_CREATED)
        return Response({'Erro': 'Saldo insuficinete para a compra com cartão'}, status=status.HTTP_201_CREATED)



class TransacaoViewSet(viewsets.GenericViewSet):
    serializer_class = TransacaoSerializer

    def create(self, request): 
        destinatario = get_object_or_404(Conta, pk=request.data.get('destinatario'))
        remetente = get_object_or_404(Conta, pk=request.data.get('conta'))
        quantia = Decimal(request.data.get('quantia'))

        if remetente.saldo >= quantia:
            remetente.saldo -= quantia
            remetente.save()
            destinatario.saldo += quantia
            destinatario.save()

            fatura_destinatario = Fatura.objects.create(
                conta = destinatario,
                tipo = 'entrada',
                valor = quantia,
                saldo = destinatario.saldo
            )

            fatura_remetente = Fatura.objects.create(
                conta = remetente,
                tipo = 'saída',
                valor = quantia,
                saldo = remetente.saldo
            )
            return Response({'Sucesso': 'Trânsferencia realizada com sucesso'}, status=status.HTTP_201_CREATED)
        return Response({'Erro': 'Saldo insuficinete para a trânsferencia'}, status=status.HTTP_201_CREATED)
    

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    def create(self, request, *args, **kwargs):
        conta = get_object_or_404(Conta, pk=request.data.get('conta'))
        quantia = Decimal(request.data.get('quantia'))
        salario = Decimal(request.data.get('salario'))

        if quantia < (salario * 3) + (conta.saldo * 3):
            aprovado = True
            response = Response({'Sucesso': 'Emprestimo realizado com sucesso'}, status=status.HTTP_201_CREATED)
        else:
            aprovado = False
            response = Response({'Error': 'Valor solicitado ultrapassa 3 vezes o seu salário + 3 vezes o seu saldo atual!'}, status=status.HTTP_201_CREATED)
            
        
        emprestimo = Emprestimo.objects.create(
            conta = conta,
            quantia = quantia,
            aprovado = aprovado
        )

        if aprovado:
            conta.saldo += quantia
            conta.save()

            fatura = Fatura.objects.create(
                conta = conta,
                tipo = 'emprestimo',
                valor = quantia,
                saldo = conta.saldo
            )

        return response


class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer

    def get_queryset(self):
        conta = self.request.query_params.get('conta')
        cartao = self.request.query_params.get('cartao')
        queryset = Fatura.objects.all()
        if conta:
            queryset = queryset.filter(conta=conta)
        if cartao:
            queryset = queryset.filter(tipo='cartao')
        return queryset