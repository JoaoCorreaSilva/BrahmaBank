from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register('contas', ContaViewSet, basename='contas')
router.register('cartoes', CartaoViewSet, basename='cartoes')
router.register('transacoes', TransacaoViewSet, 'transacoes')
router.register('trasacoes-cartao', TransacaoCartaoViewSet, basename='transacoes-cartoes')
router.register('emprestimos', EmprestimoViewSet, basename='emprestimos')
router.register('faturas', FaturaViewSet, basename='faturas')