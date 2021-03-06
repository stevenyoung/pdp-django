from django.test import LiveServerTestCase
from selenium import webdriver
import unittest


class HomePageVisitTestCase(unittest.TestCase):
  """docstring for HomePageVisitTestCase"""

  def setUp(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome Canary.app/'
    chrome_options.binary_location += 'Contents/MacOS/Google Chrome Canary'
    self.browser = webdriver.Chrome(chrome_options=chrome_options)

  def tearDown(self):
    self.browser.quit()

  def test_can_visit_home_page(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('places home', self.browser.title)


class HomePageLiveServerTestCase(LiveServerTestCase):

  def setUp(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome Canary.app/'
    chrome_options.binary_location += 'Contents/MacOS/Google Chrome Canary'
    self.browser = webdriver.Chrome(chrome_options=chrome_options)

  def tearDown(self):
    self.browser.quit()

  def test_can_open_home_page(self):
    self.browser.get(self.live_server_url)
    self.assertIn('places home', self.browser.title)

  def test_can_add_a_new_place_from_home_page(self):
    self.browser.get(self.live_server_url)
    self.assertIn('places home', self.browser.title)
    self.fail('finish this test')

  def test_can_get_user_location_from_home_page(self):
    self.fail('finish this test')


class HomePageSearchTestCase(LiveServerTestCase):

  def setUp(self):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/Applications/Google Chrome Canary.app/'
    chrome_options.binary_location += 'Contents/MacOS/Google Chrome Canary'
    self.browser = webdriver.Chrome(chrome_options=chrome_options)

  def tearDown(self):
    self.browser.quit()

  def test_can_search_via_post(self):
    self.fail('finish it!')
