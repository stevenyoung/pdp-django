from django.test import Client
from django.test import TestCase

from places.models import Scene


class NewSceneEndpointTest(TestCase):
  def test_endpoint_post_redirects_to_home_page(self):
    response = self.client.post('/places/new', {'title': 'new title'})
    self.assertEqual(response.url, '/')
    self.assertEqual(response.status_code, 302)


class HomePageTest(TestCase):

 def test_uses_home_template(self):
  response = self.client.get('/')
  self.assertTemplateUsed(response, 'index.html')


class NewSceneTest(TestCase):

  def test_can_save_a_POST_request(self):
    data = {
      'artist': {'full_name': 'Bad Brains'},
      'description': 'can save a post request',
      'lng': -122.41575,
      'lat': 37.749202,
      'artwork': 'Banned in D.C.'
    }
    self.client.post('/places/new', data=data)

    self.assertEqual(Scene.objects.count(), 1)
    new_item = Scene.objects.first()
    self.assertEqual(new_item.id, 1)
    self.assertEqual(new_item.description, 'can save a post request')
    self.assertEqual(new_item.longitude, -122.41575)
    self.assertEqual(new_item.latitude, 37.749202)

  def test_redirects_after_POST(self):
    c = Client()
    data = {
      'artist': {'full_name': 'Bad Brains'},
      'description': 'can save a post request',
      'lng': -122.41575,
      'lat': 37.749202,
      'artwork': 'Banned in D.C.'
    }
    response = c.post('/places/new', data=data)
    newest_scene_id = Scene.objects.count()
    newest_scene_url = '/places/' + newest_scene_id + '/'
    self.assertEqual(response.url, newest_scene_url)
    self.assertEqual(response.status_code, 302)

  def test_invalid_scenes_arent_saved(self):
    self.client.post('/places/new', data={'item_text': 'invalid field',
                                          'lng': -122.41575,
                                          'lat': 37.749202})
    self.assertEqual(Scene.objects.count(), 0)

  def test_validation_errors_are_sent_back_to_home_page_template(self):
    response = self.client.post('/places/new',
                                data={'description': 'incomplete data should redirect'})
    self.assertEqual(Scene.objects.count(), 0)
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], '/')


class SearchViewsTest(TestCase):
  """docstring for SearchViewsTest"""
  def test_can_search_for_a_term(self):
    response = self.client.get('/places/search/blue')
    self.assertEqual(response.status_code, 200)
