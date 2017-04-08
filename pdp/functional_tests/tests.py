from selenium import webdriver
import unittest


class HomePageVisitTestCase(unittest.TestCase):
  """docstring for HomePageVisitTestCase"""

  def setUp(self):
    self.browser = webdriver.Chrome()

  def tearDown(self):
    self.browser.quit()

  def test_can_visit_home_page(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('places home', self.browser.title)
