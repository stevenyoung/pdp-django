from django.test import TestCase
from django.utils.html import escape

from places.models import Scene
from places.models import Book
from places.models import Author


class HomePageTest(TestCase):

 def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


class NewSceneTest(TestCase):

  def test_can_save_a_POST_request(self):
    self.client.post('/places/new',
                     data={'description': 'a new scene described',
                           'lng': -122.41575,
                           'lat': 37.749202})
    self.assertEqual(Scene.objects.count(), 1)
    new_item = Scene.objects.first()
    self.assertEqual(new_item.description, 'a new scene described')
    self.assertEqual(new_item.longitude, -122.41575)
    self.assertEqual(new_item.latitude, 37.749202)

  def test_redirects_after_POST(self):
    response = self.client.post('/places/new',
                                data={'description': 'a new scene described',
                                      'lng': -122.41575,
                                      'lat': 37.749202})
    new_scene = Scene.objects.first()
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/places/%d/' % (new_scene.id,))

  def test_validation_errors_are_sent_back_to_home_page_template(self):
    response = self.client.post('/places/new',
                                data={'description': 'a new scene described'})
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'home.html')
    expected_error = escape("You can't have an empty list item")
    self.assertContains(response, expected_error)

  def test_invalid_scenes_arent_saved(self):
    self.client.post('/places/new', data={'item_text': '',
                                          'lng': -122.41575,
                                          'lat': 37.749202})
    self.assertEqual(Scene.objects.count(), 0)
