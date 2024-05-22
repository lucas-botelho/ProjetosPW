
from django.urls import path
from . import views

app_name = 'bandas'

urlpatterns = [
    path('', views.band_list_view, name='band_list'),
    path('band/<int:band_id>/', views.band_detail_view, name='band_detail'),
    path('album/<int:album_id>/', views.album_view, name='album_detail'),
    path('songs/<int:song_id>/', views.song_details, name='song_detail'),
    path('songs/create/', views.createAlbum, name='create_song'),
    path('bands/create/', views.createBand, name='create_band'),
    path('albums/create/', views.createAlbum, name='create_album'),
    path('albums/<int:album_id>/edit/', views.edit_album, name='edit_album'),
    path('bands/<int:band_id>/edit/', views.edit_band, name='edit_band'),
    path('songs/<int:song_id>/edit/', views.edit_song, name='edit_song'),
    path('songs/<int:song_id>/delete/', views.delete_song, name='delete_song'),
    path('bands/<int:band_id>/delete/', views.delete_band, name='delete_band'),
    path('albums/<int:album_id>/delete/', views.delete_album, name='delete_album'),

]
