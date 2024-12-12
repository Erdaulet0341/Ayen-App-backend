from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from api.views import GenreViewSet, CountryViewSet, ArtistViewSet, AlbumViewSet, TrackViewSet, PodcastViewSet
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="Ayen API",
        default_version='v1',
        description="API documentation",
        license=openapi.License(name="IOS License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'artists', ArtistViewSet, basename='artist')
router.register(r'albums', AlbumViewSet, basename='album')
router.register(r'tracks', TrackViewSet, basename='track')
router.register(r'podcasts', PodcastViewSet, basename='podcast')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
