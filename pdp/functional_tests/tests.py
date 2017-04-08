from selenium import webdriver
import unittest


class HomePageVisitTestCase(unittest.TestCase):
  """docstring for HomePageVisitTestCase"""

  def setUp(self):
    self.browser = webdriver.Chrome()

  def tearDown(self):
    self.browser.quit()
