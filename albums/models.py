from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Genre(models.Model):
    style = models.CharField(max_length=200)
    def __str__(self):
        return self.style

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    runtime_ms = models.IntegerField()
    def __str__(self):
        return self.song_title

class Play(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    position = models.IntegerField()

class Playlist(models.Model):
    playlist_title = models.CharField(max_length=200)
    songs = models.ManyToManyField(Play)
    current_position = models.IntegerField()
