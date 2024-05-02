
from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('', views.band_list_view, name='band_list'),
    path('band/<int:band_id>/', views.band_detail_view, name='band_detail'),
    path('album/<int:album_id>/', views.album_view, name='album_detail'),
    path('songs/<int:song_id>/', views.song_details, name='song_detail'),
]
