#!/usr/bin/env python
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import Functional_Test

class ItemValidationTest(Functional_Test):
    def test_cannot_add_empty_list_item(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda : self.assertEqual(self.browser.find_element_by_css_selector('.has-error').text, "You can't have an empty list item"))

        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.wait_for_row_in_list_table('1: Buy milk')

        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda : self.assertEqual(self.browser.find_element_by_css_selector(".has-error"), "You can't have an empty list item"))

        self.browser.find_element_by_id("id_new_item").send_keys("Make tea\n")
        self.wait_for_row_in_list_table("1: Buy milk")
        self.wait_for_row_in_list_table("2: Make tea")

        self.fail("write test")
