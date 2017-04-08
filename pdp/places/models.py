from django.db import models


class Song(models.Model):
  title = models.TextField(default='')
  composer = models.TextField(default='')
  performer = models.TextField(default='')


class Book(models.Model):
  title = models.TextField(default='')
  author = models.TextField(default='')


class Author(models.Model):
  first_name = models.TextField(default='')
  last_name = models.TextField(default='')
  full_name = models.TextField(default='')


class Scene(models.Model):
  book = Book()
  author = Author()
  description = models.TextField(default='')
  latitude = models.FloatField()
  longitude = models.FloatField()
