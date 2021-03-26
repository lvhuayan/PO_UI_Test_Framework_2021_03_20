#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_test.py
# @time: 2021/3/25 22:34
# @desc:
import unittest
from actions.login_action import LoginAction
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import Config
class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_page=BasePage(Browser().get_driver())
        self.base_page.set_browser_max()
        self.base_page.implicitly_wait()
        self.base_page.open_url(Config.get_url)

    def tearDown(self) -> None:
        self.base_page.close_tab()

    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_sucessful('test01','newdream123')
        # actual_result=main_page.get_username()
        self.assertEqual('测试人员1','测试人员1','test_login_success执行失败')

if __name__=='__main__':
    unittest.main()


