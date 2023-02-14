from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.exceptions import APIException

from .models import *
from .serializers import *


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    @action(detail=False, methods=['get'], url_path='get_albums/(?P<pk>[^/.]+)')
    def get_albums(self, request, pk=None):
        if not pk:
            raise APIException(detail="Please provide author's primary key", code=400)

        albums = Album.objects.filter(author=pk)
        serialized_albums = AlbumSerializer(albums, many=True).data
        return Response(serialized_albums)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    @action(detail=False, methods=['get'], url_path='get_songs/(?P<pk>[^/.]+)')
    def get_songs(self, request, pk=None):
        if not pk:
            raise APIException(detail="Please provide album's primary key", code=400)

        song_entries = SongEntry.objects.filter(album=pk)
        serialized_song_entries = SongEntrySerializer(song_entries, many=True).data
        return Response(serialized_song_entries)


class SongEntryViewSet(ModelViewSet):
    queryset = SongEntry.objects.all()
    serializer_class = SongEntrySerializer

    permission_classes = [AllowAny]


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    permission_classes = [AllowAny]
