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
from common.selenium_base_case import SeleniumBaseCase
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage


class QuitTest(SeleniumBaseCase):

    def test_quit(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.default_login()
        quit_action=QuitAction(main_page.driver)
        login_page=quit_action.quit()
        actual_result=login_page.get_title()
        self.assertEqual(actual_result.__contains__('用户登录'),True,'test_quit执行失败')


if __name__=='__main__':
    unittest.main()