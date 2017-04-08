from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from places.views import home_page

from places.models import Scene
from places.models import Author
from places.models import Book


class HomePageTest(TestCase):

  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_can_save_from_post(self):
    request = HttpRequest()
    request.method = 'POST'
    request.POST['post_data'] = 'data from post'
    response = home_page(request)
    self.assertIn('data from post', response.content.decode())


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
