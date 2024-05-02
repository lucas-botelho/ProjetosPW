from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
    path('lista_filmes/', views.lista_filmes, name='lista_filmes'),
    path('filme/<int:filme_id>/', views.filme_detail, name='filme_detail'),

]
