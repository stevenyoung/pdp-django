from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
  first_name = models.TextField(default='')
  last_name = models.TextField(default='')
  full_name = models.TextField(default='')


class Artwork(models.Model):
  title = models.TextField(default='')
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
  artist = models.ForeignKey(Artist, default=None)
  artwork = models.ForeignKey(Artwork, default=None)
  description = models.TextField(default='')
  notes = models.TextField(default='')
  latitude = models.FloatField()
  longitude = models.FloatField()
  submitted_by = User()
