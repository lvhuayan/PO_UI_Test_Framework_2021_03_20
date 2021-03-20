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
from common.element_data_utils import ElementDataUtils

class LoginPage(BasePage):
    def __init__(self,driver):
        # super(LoginPage, self).__init__(self,driver)
        super().__init__(driver)
        # self.username_inputbox={'element_name':'用户名输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@id="account"]',
        #                         'timeout':5
        #                         }
        # self.password_inputbox={'element_name':'密码输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@name="password"]',
        #                         'timeout':4
        #                         }
        # self.login_button={'element_name':'登录按钮',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//button[@id="submit"]',
        #                         'timeout':3
        #                         }
        elements=ElementDataUtils('login_page').get_element()
        self.username_inputbox=elements['username_inputbox']
        self.password_inputbox=elements['password_inputbox']
        self.login_button=elements['login_button']

    def input_username(self,username): #输入用户名  #方法==》控件的操作
        self.input(self.username_inputbox,username)

    def input_password(self,password):#输入密码
        self.input(self.password_inputbox,password)

    def click_login(self):#点击登录
        self.click(self.login_button)

if __name__=='__main__':
    driver=Browser().get_driver()
    login_page=LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
