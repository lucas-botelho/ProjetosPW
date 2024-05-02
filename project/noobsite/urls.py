from django.urls import path
from . import views  # importamos views para poder usar as suas funções

urlpatterns = [
      path('', views.index_view, name='noobsite')
]