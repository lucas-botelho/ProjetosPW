from django.urls import path
from . import views

app_name = 'curso' 

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_detail_view, name='curso_detail'),
    path('projeto/<int:projeto_id>/', views.projeto_detail_view, name='projeto_detail'),
]