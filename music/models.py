from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title

class Folder(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Music, related_name='folders')

    def __str__(self):
        return self.name
