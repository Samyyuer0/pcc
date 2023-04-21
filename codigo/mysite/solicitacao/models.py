from django.db import models
from usuarios.models import Pessoa, Instituicao

class Peruca(models.Model):
    cor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    escolhasTamanho = [
        ('C', 'Curto'),
        ('M', 'Médio'),
        ('C', 'Longo'),
    ]
    tamanho = models.CharField(max_length=1, choices=escolhasTamanho)

class Solicitacao(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    perucas = models.ManyToManyField(Peruca)

    data_solicitacao = models.DateTimeField(auto_now_add=True)
    codRastreio = models.CharField(max_length=20)
    quest1 = models.TextField()
    quest2 = models.TextField()
    quest3 = models.TextField()
    opcoesStatus = [
        ('analise', 'Solicitação em análise'),
        ('aprovado', 'Solicitação aprovada'),
        ('rejeitado', 'Solicitação negada'),
        ('caminho', 'Encomenda à caminho'),
        ('recebido', 'Encomenda recebida'),
    ]
    status = models.CharField(max_length=10, choices=opcoesStatus)

