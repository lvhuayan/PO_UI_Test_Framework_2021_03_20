#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_page.py
# @time: 2021/3/16 13:33
# @desc:
import os
from selenium import webdriver
from common.base_page import BasePage
from common.browser import Browser
from common.element_data_utils_old import ElementDataUtils

#测试base_page中 鼠标键盘封装 方法是否正确

class Sample05(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements=ElementDataUtils('sample05','sample05_page').get_element()
        self.login_button=elements['login_button']
        self.Language_select_button=elements['Language_select_button']
        self.Language_select=elements['Language_select']

    def click_login(self,seconds):#点击登录
        self.long_press_element(self.login_button,seconds)

    def select_language(self,language):
        self.move_to_element_by_mouse(self.Language_select_button)
        self.Language_select['locator_value']=self.Language_select['locator_value']%language
        self.click(self.Language_select)






if __name__=='__main__':
    driver=Browser().get_driver()
    login_page=Sample05(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao4/www/user-login-L3plbnRhbzQvd3d3L215Lmh0bWw=.html')
    login_page.implicitly_wait()
    login_page.select_language('English')

