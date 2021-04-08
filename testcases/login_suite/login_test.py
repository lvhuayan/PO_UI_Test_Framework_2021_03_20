#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_test_old.py
# @time: 2021/3/25 22:34
# @desc:
import unittest
from actions.login_action import LoginAction
from common.base_page import BasePage
from common.browser import Browser
from common.config_utils import Config
from common.selenium_base_case import SeleniumBaseCase


class LoginTest(SeleniumBaseCase):
    # def setUp(self) -> None:
    #     super().setUp()
    #     print('hello')

    def test_login_success(self):
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_sucessful('test01','newdream123')
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,'测试人员1','test_login_success执行失败')

    def test_login_fail(self):
        login_action = LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail('test01','newdream12')
        self.assertEqual(actual_result,'登录失败，请检查您的用户名或密码是否填写正确。','test_login_fail执行失败')


if __name__=='__main__':
    unittest.main()


