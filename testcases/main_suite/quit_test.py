#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_test_old.py
# @time: 2021/3/25 22:34
# @desc:
import unittest
from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import Config
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page_old import MainPage


class  QuitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page=BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(Config.get_url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_quit(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.default_login()
        quit_action=QuitAction(main_page.driver)
        login_page=quit_action.quit()
        actual_result=login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'),True,'test_quit执行失败')


if __name__=='__main__':
    unittest.main()