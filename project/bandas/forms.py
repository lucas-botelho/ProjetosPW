from django import forms
from .models import *

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'spotify_link', 'duration']

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name', 'genre', 'formed_in', 'photo', 'info', 'nacionality']

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'release_year', 'cover', 'band']
