from django.urls import path
from . import views

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('curso/<int:curso_id>/', views.curso_detail_view, name='curso_detail'),
]