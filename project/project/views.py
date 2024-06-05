from django.shortcuts import render

from artigos.models import *

from django.conf import settings
INSTALLED_APPS = settings.INSTALLED_APPS

class AppData:
    def __init__(self, url, name):
        self.url = url
        self.name = name


def index_view(request):
    
    apps = []

    autenticacao = False
    for app in INSTALLED_APPS:
        if autenticacao:
            apps.append(AppData(url = f'{app}:index', name = app.capitalize()))
        else:
            if app == 'autenticacao':
                autenticacao = True

    context = {
        'apps': apps,
    }
    
    return render(request, 'project/index.html', context)