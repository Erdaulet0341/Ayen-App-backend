from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="country_artists")
    bio = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="albums")
    release_date = models.DateField()
    cover_image = models.CharField(max_length=1000, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="tracks")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="tracks")
    genre = models.ManyToManyField(Genre, related_name="tracks")
    audio_file = models.FileField(upload_to="tracks/")
    cover_image = models.CharField(max_length=1000, blank=True, null=True)
    length = models.CharField(max_length=255)
    release_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="tracks")
    play_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lyrics(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE, related_name="lyrics")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.track.title} - Lyric"

    class Meta:
        verbose_name_plural = "Lyrics"


class Podcast(models.Model):
    title = models.CharField(max_length=255)
    video_url = models.CharField(max_length=1000, blank=True, null=True)
    release_date = models.DateField()
    cover_image = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
