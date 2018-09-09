# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.utils.translation import activate
from django.utils import formats
from datetime import date

chromedriver = '../../../../driver/chromedriver'

class HomeNewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(3)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def test_home_title(self):
        self.browser.get(self.get_full_url('home'))
        self.assertIn('TaskBuster', self.browser.title)

    def test_h1_css(self):
        self.browser.get(self.get_full_url('home'))
        h1= self.browser.find_element_by_tag_name('h1')
        self.assertEqual(h1.value_of_css_property('color'),
                'rgba(200, 50, 255, 1)')

    def test_home_files(self):
        self.browser.get(self.live_server_url + '/robots.txt')
        self.assertNotIn('Not Found', self.browser.title)
        self.browser.get(self.live_server_url + '/humans.txt')
        self.assertNotIn('Not Found', self.browser.title)

    def test_localization(self):
        today = date.today()
        for lang in ['en', 'ca']:
            activate(lang)
            self.browser.get(self.get_full_url("home"))
            local_date = self.browser.find_element_by_id("local-date")
            non_local_date = self.browser.find_element_by_id("non-local-date")
            self.assertEqual(formats.date_format(today, use_l10n=True),
                                  local_date.text)
            # self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)
            self.assertEqual(today.strftime('%Y-%m-%d'), non_local_date.text)

    def test_time_zone(self):
        self.browser.get(self.get_full_url('home'))
        tz = self.browser.find_element_by_id('time-tz').text
        utc = self.browser.find_element_by_id('time-utc').text
        ny = self.browser.find_element_by_id('time-ny').text
        self.assertNotEqual(tz, utc)
        self.assertNotIn(ny, [tz, utc])


class TestGoogleLogin(StaticLiveServerTestCase):

    fixtures = ['allauth_fixture']
    port = 8081

    def setUp(self):
        self.browser = webdriver.Chrome(chromedriver)
        self.browser.implicitly_wait(2)
        self.browser.wait = WebDriverWait(self.browser, 5)
        activate('en')

    def tearDown(self):
        self.browser.quit()

    def get_element_by_id(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
                    (By.ID, element_id)))

    def get_button_by_id(self, element_id):
        return self.browser.wait.until(EC.element_to_be_clickable(
                    (By.ID, element_id)))

    def get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def get_element_by_xpath(self, element_id):
        return self.browser.wait.until(EC.presence_of_element_located(
                    (By.XPATH, element_id)))

    def get_google_button_by_xpath(self, element_xpath):
        return self.browser.wait.until(EC.element_to_be_clickable(
                    (By.XPATH, element_xpath)))

    def get_google_button_by_class_name(self, element_class_name):
        return self.browser.wait.until(EC.element_to_be_clickable(
                    (By.CLASS_NAME, element_class_name)))

    def user_login(self):
        import json
        with open('taskbuster/fixtures/google_user.json') as f:
            credentials = json.loads(f.read())
        self.get_element_by_xpath('//*[@id="identifierId"]').send_keys(credentials['Email'])
        self.get_google_button_by_xpath('//*[@id="identifierNext"]/content/span').click()
        self.get_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(credentials['Passwd'])
        self.get_google_button_by_class_name('ANuIbb IdAqtf').click()
        return

    def test_google_login(self):
        self.browser.get(self.get_full_url('home'))
        google_login = self.get_element_by_id('google_login')
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('logout')
        self.assertEqual(
                google_login.get_attribute('href'),
                self.live_server_url + '/accounts/google/login')
        google_login.click()
        self.user_login()
        with self.assertRaises(TimeoutException):
            self.get_element_by_id('google_login')
        google_logout = self.get_element_by_id('logout')
        google_logout.click()
        google_login = self.get_element_by_id('google_login')
