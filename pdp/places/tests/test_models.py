from django.test import TestCase

from places.models import Scene
from places.models import Author
from places.models import Book


class SceneModelTest(TestCase):

  def test_saving_and_retrieving_scene_descriptions(self):
    scene = Scene()
    scene.description = 'the first list item described'
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.save()


class AuthorModelTest(TestCase):

  def test_saving_and_retrieving_scene_descriptions(self):
    first_item = Author()
    first_item.description = 'the first list item described'
    first_item.save()


class BookModelTest(TestCase):

  def test_saving_and_retrieving_scene_descriptions(self):
    first_item = Book()
    first_item.description = 'the first list item described'
    first_item.save()
