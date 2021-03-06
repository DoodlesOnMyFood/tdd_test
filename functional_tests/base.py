#!/usr/bin/env python
import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchElementException, StaleElementReferenceException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time

MAXWAIT = 3

class Functional_Test(StaticLiveServerTestCase):
    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')
    def setUp(self):
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server 

    def tearDown(self):
        self.browser.quit()
    
    def wait_to_be_logged_in(self, email):
        self.wait_for(lambda: self.browser.find_element_by_link_text("Log out"))
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    def wait_to_be_logged_out(self, email):
        self.wait_for(lambda: self.browser.find_element_by_name("email"))
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException, NoSuchElementException) as e:
                if time.time() - start_time > MAXWAIT:
                    raise e
                time.sleep(.5)

    def wait_for(self, assertion):
        start_time = time.time()
        while True:
            try:
                assertion()
                return
            except (AssertionError, NoSuchElementException, StaleElementReferenceException) as e:
                if time.time() - start_time > MAXWAIT:
                    raise e
                time.sleep(.5)
