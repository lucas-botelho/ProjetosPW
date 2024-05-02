from django.urls import path
from . import views

app_name = 'artigos'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail')
]
