from django.contrib.auth.models import User
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, unique=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    escolhaRegiao = [
        ('NO', 'Norte'),
        ('NE', 'Nordeste'),
        ('SE', 'Sudeste'),
        ('CO', 'Centro-Oeste'),
        ('SU', 'Sul'),
    ]
    rua = models.CharField(max_length=255)
    num = models.IntegerField
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    regiao = models.CharField(max_length=2, choices=escolhaRegiao, default='NO')
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'{self.rua}, {self.bairro}, {self.cidade} - {self.estado}'

class Depoimento(models.Model):
    relato = models.TextField()
    data = models.DateField(auto_now_add=True)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.relato