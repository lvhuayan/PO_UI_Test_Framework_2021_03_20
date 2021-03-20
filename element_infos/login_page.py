#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: login_page.py
# @time: 2021/3/16 13:33
# @desc:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

current_path=os.path.dirname(__file__)
driver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')

class LoginPage:
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.username_inputbox=self.driver.find_element(By.XPATH,'//input[@id="account"]') #属性==》页面的控件
        self.password_inputbox=self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.login_button=self.driver.find_element(By.XPATH,'//button[@id="submit"]')

    def input_username(self,username): #输入用户名  #方法==》控件的操作
        self.username_inputbox.send_keys(username)

    def input_password(self,password):#输入密码
        self.password_inputbox.send_keys(password)

    def click_login(self):#点击登录
        self.login_button.click()

if __name__=='__main__':
    login_page=LoginPage()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
