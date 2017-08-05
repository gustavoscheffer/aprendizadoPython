from django.db import models


class Aluno(models.Model):

    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Treino(models.Model):
    nome = models.CharField(max_length=100)
    observacao = models.CharField(max_length=300)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
