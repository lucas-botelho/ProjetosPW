from curso.models import *
import json

with open('curso/json/curso.json') as f:
    dados = json.load(f)

    print(dados)