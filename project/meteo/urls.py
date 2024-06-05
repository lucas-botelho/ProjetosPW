from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('previsao-lisboa/', views.previsao_lisboa, name='previsao_lisboa'),
]