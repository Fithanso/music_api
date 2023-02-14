from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

    def validate(self, data):
        if not data['release_year'].isdigit() or len(data['release_year']) != 4:
            raise ValidationError('Provided release_year is invalid')
        return data


class SongEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = SongEntry
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
