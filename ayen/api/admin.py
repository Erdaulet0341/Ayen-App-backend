from django.contrib import admin

from .models import Genre, Country, Artist, Album, Track, Podcast, Lyrics


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country', 'created_at')
    search_fields = ('name', 'country')
    ordering = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist', 'release_date', 'created_at')
    search_fields = ('title', 'artist__name')
    list_filter = ('release_date',)
    ordering = ('release_date',)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'album', 'artist', 'length', 'release_date', 'play_count', 'likes_count', 'created_at')
    search_fields = ('title', 'album__title', 'artist__name')
    list_filter = ('release_date', 'genre')
    ordering = ('release_date',)
    filter_horizontal = ('genre',)


@admin.register(Lyrics)
class LyricsAdmin(admin.ModelAdmin):
    list_display = ('id', 'track', 'created_at')
    search_fields = ('track__title',)
    ordering = ('track__title',)


@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    ordering = ('title',)