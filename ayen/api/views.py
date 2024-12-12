from django.db.models import Q
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .models import Genre, Country, Artist, Album, Track, Podcast
from .serializers import (GenreSerializer, CountrySerializer, ArtistSerializer, AlbumSerializer, TrackSerializer,
                          PodcastSerializer)


# Genre Views
class GenreViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


# Country Views
class CountryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


# Artist Views
class ArtistViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


# Album Views
class AlbumViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


# Track Views
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class TrackViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    @swagger_auto_schema(
        operation_description="Search tracks by track name or artist name",
        manual_parameters=[
            openapi.Parameter('query', openapi.IN_QUERY, description="Search query for track name or artist name",
                              type=openapi.TYPE_STRING)
        ]
    )
    @action(detail=False, methods=['get'], url_path='search_tracks')
    def search_tracks(self, request):
        query = request.query_params.get('query', None)

        if not query:
            return Response({"detail": "Search query is required."}, status=status.HTTP_400_BAD_REQUEST)

        tracks = Track.objects.filter(
            Q(title__icontains=query) | Q(artist__name__icontains=query)
        )

        serializer = self.get_serializer(tracks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Get tracks by country ID",
        manual_parameters=[
            openapi.Parameter('country_id', openapi.IN_QUERY, description="ID of the country",
                              type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'], url_path='get_tracks_of_country')
    def get_tracks_by_country(self, request):
        country_id = request.query_params.get('country_id')
        if not country_id:
            return Response({"detail": "Country ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        tracks = Track.objects.filter(country_id=country_id)
        serializer = self.get_serializer(tracks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Get tracks by artist ID",
        manual_parameters=[
            openapi.Parameter('artist_id', openapi.IN_QUERY, description="ID of the artist", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'], url_path='get_tracks_of_artist')
    def get_tracks_of_artist(self, request):
        artist_id = request.query_params.get('artist_id')
        if not artist_id:
            return Response({"detail": "Artist ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        tracks = Track.objects.filter(artist_id=artist_id)
        serializer = self.get_serializer(tracks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Get tracks by album ID",
        manual_parameters=[
            openapi.Parameter('album_id', openapi.IN_QUERY, description="ID of the album", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'], url_path='get_tracks_of_album')
    def get_tracks_of_album(self, request):
        album_id = request.query_params.get('album_id')
        if not album_id:
            return Response({"detail": "Album ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        tracks = Track.objects.filter(album_id=album_id)
        serializer = self.get_serializer(tracks, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Get tracks by genre ID",
        manual_parameters=[
            openapi.Parameter('genre_id', openapi.IN_QUERY, description="ID of the genre", type=openapi.TYPE_INTEGER)
        ]
    )
    @action(detail=False, methods=['get'], url_path='get_tracks_of_genre')
    def get_tracks_of_genre(self, request):
        genre_id = request.query_params.get('genre_id')
        if not genre_id:
            return Response({"detail": "Genre ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        tracks = Track.objects.filter(genre__id=genre_id)
        serializer = self.get_serializer(tracks, many=True)
        return Response(serializer.data)


# Podcast Views
class PodcastViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
