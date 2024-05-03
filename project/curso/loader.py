from curso.models import *
import json

curso = Curso.objects.create(
    name='Example Course',
    objectives='Example objectives of the course.',
    presentation='Example presentation of the course.',
    competences='Example competences of the course.'
)

with open('curso/json/curso.json') as f:
    dados = json.load(f)

    print(dados)