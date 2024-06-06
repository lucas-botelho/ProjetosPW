from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('previsao-lisboa/', views.previsao_lisboa, name='index'),
    path('previsao/', views.previsao, name='previsao'),
    path('previsao/<int:city_id>/', views.previsao_cidade, name='previsao_cidade'),
    path('api/listacidades/', views.lista_cidades, name='lista_cidades'),
    path('api/tempo/<int:city_id>/', views.tempo_cidade, name='tempo_cidade'),
]