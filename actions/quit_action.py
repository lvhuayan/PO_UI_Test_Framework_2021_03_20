#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: quit_action.py
# @time: 2021/3/27 20:23
# @desc:
from actions.login_action import LoginAction
from common.browser import Browser
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import Config

class QuitAction:
    def __init__(self,driver):
        self.main_page=MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit()
        return LoginPage(self.main_page.driver)

if __name__=='__main__':
    driver=Browser().get_driver()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    driver.maximize_window()
    driver.implicitly_wait(5)
    login_action=LoginAction(driver)
    main_page=login_action.default_login()
    main_page.implicitly_wait(5)
    QuitAction(main_page.driver).quit()
