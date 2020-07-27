#!/usr/bin/env python
from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import Functional_Test

class ItemValidationTest(Functional_Test):
    @skip
    def test_cannot_add_empty_list_item(self):
        self.fail("write test")
