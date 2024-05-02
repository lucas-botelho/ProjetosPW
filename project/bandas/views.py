from django.shortcuts import render
from .models import Band, Album, Song

def index_view(request):
    context = {}
    return render(request, 'bandas/index.html', context)

def band_list_view(request):
    bands = Band.objects.all()
    context = {'bands': bands}
    return render(request, 'bandas/bands.html', context)

def album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    songs = Song.objects.filter(album=album)
    context = {'album': album, 'songs': songs}
    return render(request, 'bandas/album.html', context)

def song_details(request, song_id):
    song = Song.objects.get(id=song_id)
    album = Album.objects.get(song = song)
    context = {'song': song, 'album' : album}

    return render(request, 'bandas/song_details.html', context)

def band_detail_view(request, band_id):
    band = Band.objects.get(pk=band_id)
    albuns = Album.objects.filter(band=band)
    context = {'band': band, 'albums': albuns}
    return render(request, 'bandas/band_detail.html', context)
