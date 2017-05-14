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


SAMPLES = [{'artist': {'full_name': 'Bad Brains'},
            'description': 'can save a post request',
            'lng': -122.41575,
            'lat': 37.749202,
            'artwork': 'Banned in D.C.'
            },
           {'artist': {'full_name': 'Alien Life Form'},
            'description': 'can save a post request',
            'lng': -122.41575,
            'lat': 37.749202,
            'artwork': 'ALF Sings!'
            }]


class NewSceneTest(TestCase):

  def setUp(self):
    self.sample_data = [{
      'artist': {'full_name': 'Bad Brains'},
      'description': 'can save a post request',
      'lng': -122.41575,
      'lat': 37.749202,
      'artwork': 'Banned in D.C.'
    }, {
      'artist': {'full_name': 'Alien Life Form'},
      'description': 'can save a post request',
      'lng': -122.41575,
      'lat': 37.749202,
      'artwork': 'ALF Sings!'
    }]
    Scene.objects.all().delete()

  def test_can_save_a_POST_request(self):
    self.assertEqual(Scene.objects.count(), 0)
    self.client.post('/places/new', data=self.sample_data[1])
    self.assertEqual(Scene.objects.count(), 1)
    new_item = Scene.objects.first()
    self.assertEqual(new_item.artwork.title, 'ALF Sings!')
    self.assertEqual(new_item.description, 'can save a post request')
    self.assertEqual(new_item.longitude, -122.41575)
    self.assertEqual(new_item.latitude, 37.749202)

  def test_redirects_to_new_scene_after_POST(self):
    self.assertEqual(Scene.objects.count(), 0)
    c = Client()
    response = c.post('/places/new', data=self.sample_data[0])
    self.assertEqual(response.status_code, 302)
    self.assertRegex(response.url, '^/places/[0-9]')

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


class SceneViewTest(TestCase):

  def test_uses_scene_template(self):
    self.client.post('/places/new', data=SAMPLES[1])
    self.assertEqual(Scene.objects.count(), 1)
    response = self.client.get('/places/1')
    self.assertTemplateUsed(response, 'scene.html')

  def test_can_view_scene(self):
    self.client.post('/places/new', data=SAMPLES[1])
    self.assertEqual(Scene.objects.count(), 1)
    response = self.client.get('/places/1')
    self.assertEqual(response.status_code, 301)
    self.assertContains(response, 'Banned', status_code=301)
