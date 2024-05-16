from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

class DisciplinaViewModel:
    def __init__(self, disciplina, projetos):
        self.info = disciplina
        self.projetos = projetos

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/cursos.html', {'cursos': cursos})

def curso_detail_view(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    disciplinas = Disciplina.objects.filter(course = curso)
    disciplinasLista = []

    for d in disciplinas:
        disciplinasLista.append(DisciplinaViewModel(d, Projeto.objects.filter(disciplina = d)))

    return render(request, 'curso/curso_detail.html', {'curso': curso, 'disciplinasLista': disciplinasLista})
