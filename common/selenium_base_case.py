#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: selenium_base_case.py
# @time: 2021/3/29 17:07
# @desc:
import unittest

from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import Config


class SeleniumBaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.url=Config.get_url

    def setUp(self) -> None:
        self.base_page=BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(self.url)

    def tearDown(self) -> None:
        self.base_page.close_tab()