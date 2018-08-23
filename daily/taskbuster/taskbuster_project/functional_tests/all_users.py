# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        chromedriver = '../../../../driver/chromedriver'
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django: the Web framework for perfectionists with deadlines.', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
