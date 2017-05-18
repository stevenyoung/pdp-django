from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import User


class Artist(models.Model):
  first_name = models.TextField(default='')
  last_name = models.TextField(default='')
  full_name = models.TextField(default='')

  def save(self, *args, **kwargs):
    if self.full_name == '':
      self.full_name = '{} {}'.format(self.first_name, self.last_name)
    super().save(*args, **kwargs)


class Artwork(models.Model):
  title = models.TextField(default='Untitled')
  artist = models.ForeignKey(Artist, default=None)


class Director(Artist):
  pass


class Editor(Artist):
  pass


class Composer(Artist):
  pass


class Performer(Artist):
  pass


class Author(Artist):
  pass


class Movie(Artwork):
  director = models.ManyToManyField(Director)
  editor = models.ManyToManyField(Editor)


class Song(Artwork):
  composer = models.ManyToManyField(Composer)
  performer = models.ManyToManyField(Performer)


class Book(Artwork):
  author = models.ManyToManyField(Author)


class Scene(models.Model):
  artwork = models.ForeignKey(Artwork, default=None)
  description = models.TextField(default='')
  notes = models.TextField(default='')
  latitude = models.FloatField()
  longitude = models.FloatField()
  submitted_by = User()
  name = models.TextField(default='')
  coordinates = PointField(geography=True, null=True, blank=True)

  def to_dict(self):
    data = {}
    data['id'] = self.id
    data['artist'] = self.artwork.artist.full_name
    data['artwork'] = self.artwork.title
    data['name'] = self.name
    data['description'] = self.description
    data['notes'] = self.notes
    data['latitude'] = self.latitude
    data['longitude'] = self.longitude
    data['loc'] = {'coordinates': [self.latitude, self.longitude],
                   'type': 'Point'}
    return data
