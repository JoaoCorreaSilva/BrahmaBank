from django.db import models
from django.contrib.auth import get_user_model

from django.contrib.auth.models import(
    AbstractUser, 
    BaseUserManager
)

from .utils.foto import *

class CustomUserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, registro, password, **extra_fields):
		if not registro:
			raise ValueError('Obrigatório passar número de registro')
		user = self.model(registro=registro, username=registro, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user
	
	def create_user(self, registro, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(registro, password, **extra_fields)
    
	def create_superuser(self, registro, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)
		extra_fields.setdefault('is_staff', True)
		
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser needs the is_superuser=True')
		
		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser needs the is_staff=True') 
		return self._create_user(registro, password, **extra_fields)
	

class CustomUser(AbstractUser):
	"""
		Customized User model
	"""
	registro = models.BigIntegerField(primary_key=True, unique=True)
	foto = models.ImageField(upload_to=upload_user_photo, blank=True, null=True)
	is_staff = models.BooleanField(default=True)

	USERNAME_FIELD = 'registro'
	REQUIRED_FIELDS = ['foto']

	def __str__(self) -> str:
		return str(self.registro)
	
	objects = CustomUserManager()
	

class Conta(models.Model):

	ACCOUNT_TYPE_CHOICES = [
		['Corrente', 'Corrente'],
		['Poupança', 'Poupança'],
	]
	
	numero = models.IntegerField(primary_key=True)
	usuario = models.ManyToManyField(get_user_model())
	agencia = models.IntegerField()
	tipo = models.CharField(max_length=8, choices=ACCOUNT_TYPE_CHOICES)
	saldo = models.DecimalField(decimal_places=2, max_digits=7)
	limite_cartao = models.DecimalField(decimal_places=2, max_digits=7)

	class Meta:
		verbose_name = 'conta'
		verbose_name_plural = 'contas'

	def __str__(self):
		return f'{self.numero}'
	

class Cartao(models.Model):

	conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
	numero = models.CharField(max_length=50)
	validade = models.DateField()
	bandeira = models.CharField(max_length=25)
	cvv = models.CharField(max_length=25)

	class Meta:
		verbose_name = 'cartão'
		verbose_name_plural = 'cartões'

	def __str__(self):
		return f'{self.numero}'
	

class Fatura(models.Model):
	conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=15)
	valor  = models.DecimalField(decimal_places=2, max_digits=7)
	saldo = models.DecimalField(decimal_places=2, max_digits=7)

	class Meta:
		verbose_name = "fatura"
		verbose_name_plural = "faturas"

	def __str__(self) -> str:
		return f'{self.conta} {self.tipo} {self.valor}'
	

class Emprestimo(models.Model):
	conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
	quantia = models.DecimalField(decimal_places=2, max_digits=7)
	aprovado = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'emprestimo'
		verbose_name_plural = 'emprestimos'

	def __str__(self):
		return f'{self.pk}'
