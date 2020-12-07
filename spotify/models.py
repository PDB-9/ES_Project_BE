from django.db import models
from django.contrib.postgres.fields import ArrayField

class Spotify(models.Model):
    acousticness = models.FloatField()
    artists = ArrayField(models.CharField(max_length=100), blank=True,)
    danceability = models.FloatField()
    duration_ms = models.IntegerField()
    energy = models.FloatField()
    explicit = models.IntegerField()
    id = models.CharField(max_length=100, primary_key=True)
    instrumentalness = models.FloatField()
    key = models.IntegerField()
    liveness = models.FloatField()
    loudness = models.FloatField()
    mode = models.IntegerField()
    name = models.CharField(max_length=100)
    popularity = models.IntegerField()
    release_date = models.DateField()
    speechiness = models.FloatField()
    tempo = models.FloatField()
    valence = models.FloatField()
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.name
