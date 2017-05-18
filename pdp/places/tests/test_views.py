from django.test import Client
from django.test import TestCase

from places.models import Artist
from places.models import Artwork
from places.models import Scene


SAMPLE_POSTS = [{'artist': {'full_name': 'Bad Brains'},
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


class HomePageTest(TestCase):

 def test_uses_home_template(self):
  response = self.client.get('/')
  self.assertTemplateUsed(response, 'index.html')


class NewSceneTest(TestCase):

  def setUp(self):
    self.sample_data = SAMPLE_POSTS
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

  def test_search_request_returns_status_200(self):
    response = self.client.get('/places/search/blue')
    self.assertEqual(response.status_code, 200)

  def test_search_request_returns_search_term(self):
    response = self.client.get('/places/search/blue')
    self.assertContains(response, '"query": "blue"')

  def test_search_returns_new_matches_with_query(self):
    artist_ = Artist.objects.create(full_name="Bad Brains")
    artwork_ = Artwork.objects.create(artist=artist_, title='Banned in D.C.')
    scene = Scene()
    scene.description = 'can save a post request'
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.artwork = artwork_
    scene.save()
    new_item = Scene.objects.first()
    response = self.client.get('/places/search/Banned')
    self.assertContains(response, '"query": "Banned"')
    self.assertContains(response, new_item.artwork.title)
    self.assertContains(response, new_item.artwork.artist.full_name)

  def test_text_queries_are_case_insensitive(self):
    artist_ = Artist.objects.create(full_name="Bad Brains")
    artwork_ = Artwork.objects.create(artist=artist_, title='Banned in D.C.')
    scene = Scene()
    scene.description = 'can save a post request',
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.artwork = artwork_
    scene.save()
    new_item = Scene.objects.first()
    response = self.client.get('/places/search/banned')
    self.assertContains(response, '"query": "banned"')
    self.assertContains(response, new_item.artwork.title)
    self.assertContains(response, new_item.artwork.artist.full_name)

  def test_can_search_places_by_coords(self):
    lat = 37.749202
    lng = -122.41575
    response = self.client.get('/places/near/%s/%s' % (lng, lat))
    self.assertEqual(response.status_code, 200)

  def test_coordinate_search_returns_query_dict(self):
    lat = 37.749202
    lng = -122.41575
    response = self.client.get('/places/near/%s/%s' % (lng, lat))
    self.assertContains(response, lat)
    self.assertContains(response, lng)


class SceneViewTest(TestCase):

  def setUp(self):
    artist_ = Artist.objects.create(full_name="Bad Brains")
    artwork_ = Artwork.objects.create(artist=artist_, title='Banned in D.C.')
    scene = Scene()
    scene.description = 'can save a post request',
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.artwork = artwork_
    scene.save()
    new_item = Scene.objects.first()
    self.new_scene_url = '/places/' + str(new_item.id)

  def test_uses_scene_template(self):
    self.assertEqual(Scene.objects.count(), 1)
    response = self.client.get(self.new_scene_url)
    self.assertTemplateUsed(response, 'scene.html')

  def test_viewing_scene_returns_status_200(self):
    response = self.client.get(self.new_scene_url)
    self.assertEqual(response.status_code, 200)

  def test_scene_view_shows_artwork_title(self):
    response = self.client.get(self.new_scene_url)
    self.assertContains(response, 'Banned')

  def test_scene_view_shows_artwork_artist(self):
    response = self.client.get(self.new_scene_url)
    self.assertContains(response, 'Bad Brains')


class SceneAPITest(TestCase):

  def setUp(self):
    artist_ = Artist.objects.create(full_name="bad brains")
    artwork_ = Artwork.objects.create(artist=artist_, title='Banned in D.C.')
    scene = Scene()
    scene.description = 'can save a post request',
    scene.longitude = -122.41575
    scene.latitude = 37.749202
    scene.artwork = artwork_
    scene.save()
    new_item = Scene.objects.first()
    self.new_scene_url = '/places/api/' + str(new_item.id)

  def test_requesting_scene_data_as_json_returns_status_200(self):
    response = self.client.get(self.new_scene_url)
    self.assertEqual(response.status_code, 200)

  def test_location_data_available_in_api_response(self):
    response = self.client.get(self.new_scene_url)
    self.assertContains(response, '-122.41575')
    self.assertContains(response, '37.749202')

  def test_artwork_data_available_in_api_response(self):
    response = self.client.get(self.new_scene_url)
    self.assertContains(response, 'bad brains')
    self.assertContains(response, 'Banned in D.C.')
