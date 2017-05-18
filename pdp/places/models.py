from django.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
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


class SceneDistanceManager(models.Manager):

  def distance_filter(self, lat, lng):
    pnt = GEOSGeometry(Point(float(lng), float(lat)))
    qs = Scene.objects.filter(coordinates__dwithin=(pnt, D(mi=100)))
    return qs


class Scene(models.Model):
  artwork = models.ForeignKey(Artwork, default=None)
  description = models.TextField(default='')
  notes = models.TextField(default='')
  latitude = models.FloatField()
  longitude = models.FloatField()
  submitted_by = User()
  name = models.TextField(default='')
  coordinates = PointField(geography=True, null=True, blank=True)
  objects = SceneDistanceManager()

  def to_dict(self):
    data = {}
    data['id'] = self.id
    data['artist'] = self.artwork.artist.full_name
    data['artwork'] = self.artwork.title
    data['name'] = self.name
    data['description'] = self.description
    data['notes'] = self.notes
    data['loc'] = {'coordinates': [self.latitude, self.longitude],
                   'type': 'Point'}
    return data

  def save(self, *args, **kwargs):
    if isinstance(self.latitude, float) and isinstance(self.longitude, float):
      self.coordinates = GEOSGeometry(Point(self.latitude, self.longitude))
      super().save(*args, **kwargs)
