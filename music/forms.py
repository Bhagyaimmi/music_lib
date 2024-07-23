from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Music, Folder

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['title', 'artist', 'genre', 'file']

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'tracks']
