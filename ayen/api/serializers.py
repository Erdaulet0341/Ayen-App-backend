from rest_framework import serializers
from .models import Genre, Country, Artist, Album, Track, Podcast


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class TrackSerializer(serializers.ModelSerializer):
    album = AlbumSerializer(read_only=True)
    artist = ArtistSerializer(read_only=True)  # Embed artist details
    genre = GenreSerializer(many=True, read_only=True)  # Embed genre details
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Track
        fields = '__all__'


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'
