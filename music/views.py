from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import User, Music, Folder
from .forms import UserRegisterForm, MusicForm, FolderForm

def home(request):
    tracks = Music.objects.all()
    return render(request, 'index.html', {'tracks': tracks})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def user_dashboard(request):
    folders = Folder.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'folders': folders})

class FolderCreateView(CreateView):
    model = Folder
    form_class = FolderForm
    template_name = 'folder_form.html'
    success_url = '/dashboard/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MusicCreateView(CreateView):
    model = Music
    form_class = MusicForm
    template_name = 'music_form.html'
    success_url = '/dashboard/'
