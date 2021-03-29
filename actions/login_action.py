#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_action.py
# @time: 2021/3/25 15:07
# @desc:
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import Config

class LoginAction:
    def __init__(self,driver):
        self.login_page=LoginPage(driver)

    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    def login_sucessful(self,username,password):
        self.login_action(username, password)
        return MainPage(self.login_page.driver)

    def login_fail(self,username,password):
        self.login_action(username,password)
        return self.login_page.get_login_fail_alert_content()

    def default_login(self):
        self.login_action(Config.get_username,Config.get_password)
        return MainPage(self.login_page.driver)

    def login_by_cookie(self):
        pass
