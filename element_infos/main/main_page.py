#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: main_page.py
# @time: 2021/3/27 16:50
# @desc:
# from actions.login_action import LoginAction
from common.base_page import BasePage
from common.browser import Browser
from common.element_data_utils import ElementDataUtils


class MainPage(BasePage):
    def __init__(self,driver):
        # super(LoginPage, self).__init__(self,driver)
        super().__init__(driver)
        elements=ElementDataUtils('main','main_page').get_element()
        self.myzone_menu=elements['myzone_menu']
        self.username_menu=elements['username_menu']
        self.quit_button=elements['quit_button']

    def goto_myzone(self):
        self.click(self.myzone_menu)

    def get_username(self):
        return self.get_text(self.username_menu)

    def click_username(self):
        self.click(self.username_menu)

    def click_quit(self):
        self.click(self.quit_button)

if __name__=='__main__':
    driver=Browser().get_driver()
    # driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    # driver.maximize_window()
    # driver.implicitly_wait(5)
    # main_page=LoginAction(driver).login_sucessful('test01','newdream123')
    # value=main_page.get_username()
    # print(value)


