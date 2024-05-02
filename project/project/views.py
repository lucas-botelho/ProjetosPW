from django.shortcuts import render

from artigos.models import *

def index_view(request):
    context = {}
    
    return render(request, 'project/index.html', context)