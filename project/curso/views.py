from django.shortcuts import render
from django.views.generic import DetailView
from .models import Curso

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/cursos.html', {'cursos': cursos})

def curso_detail_view(request, curso_id):
    curso = Curso.objects.get(pk=curso_id)
    return render(request, 'curso/curso_detail.html', {'curso': curso})
