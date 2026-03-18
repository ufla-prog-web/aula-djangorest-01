from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preço = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome