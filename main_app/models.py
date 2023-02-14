from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Album(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='albums')
    release_year = models.CharField(max_length=4)

    def __str__(self):
        return str(self.author) + ': ' + str(self.release_year)


class SongEntry(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE, related_name='song_entries')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='song_entries')
    place_in_album = models.IntegerField()

    def __str__(self):
        return str(self.song) + ' №' + str(self.place_in_album) + ' in ' + str(self.album)


class Song(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
