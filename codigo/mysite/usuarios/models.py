from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class Pessoa(AbstractBaseUser):
    # Campos personalizados da classe Pessoa
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)

    # Campos padrão da classe User
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome

class Instituicao(AbstractBaseUser):
    # Campos personalizados da classe Pessoa
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20)

    # Campos padrão da classe User
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    num = models.IntegerField
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    escolhaRegiao = [
        ('NO', 'Norte'),
        ('NE', 'Nordeste'),
        ('SE', 'Sudeste'),
        ('CO', 'Centro-Oeste'),
        ('SU', 'Sul'),
    ]
    regiao = models.CharField(max_length=2, choices=escolhaRegiao, default='NO')

    def __str__(self):
        return f'{self.rua}, {self.bairro}, {self.cidade} - {self.estado}'

class Depoimento(models.Model):
    relato = models.TextField()
    data = models.DateField(auto_now_add=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    #data_criacao = models.DateTimeField(auto_now_add=True)
    #data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.relato