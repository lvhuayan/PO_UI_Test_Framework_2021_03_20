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
from common.test_data_utils import TestDataUtils


class LoginTest(SeleniumBaseCase):
    # def setUp(self) -> None:
    #     super().setUp()
    #     print('hello')
    test_class_data=TestDataUtils('login_suite', 'LoginTest').conver_exceldata_to_testdata()


    def test_login_success(self):
        test_function_data=self.test_class_data['test_login_success']
        self._testMethodDoc=test_function_data['testName']
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_sucessful(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        actual_result=main_page.get_username()
        self.assertEqual(actual_result,test_function_data['expectResult'],test_function_data['message'])

    def test_login_fail(self):
        test_function_data = self.test_class_data['test_login_fail']
        login_action = LoginAction(self.base_page.driver)
        actual_result=login_action.login_fail(test_function_data['test_parameter'].get('username'),test_function_data['test_parameter'].get('password'))
        self.assertEqual(actual_result,test_function_data['expectResult'],test_function_data['message'])


if __name__=='__main__':
    unittest.main()


