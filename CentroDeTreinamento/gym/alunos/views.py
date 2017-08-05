from django.shortcuts import render
from .models import Aluno


def index(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/index.html', {'alunos': alunos})


def cadastra(request):
    pass


def remove(request):
    pass


def edita(request):
    pass
