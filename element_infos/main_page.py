#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: base_page.py
# @time: 2021/3/16 14:03
# @desc:
from selenium.webdriver.common.by import By
from common.log_utils import logutils
from element_infos.login_page import LoginPage

class MainPage:
    def __init__(self):
        self.login_page=LoginPage()
        self.login_page.input_username('test01')
        self.login_page.input_password('newdream123')
        self.login_page.click_login()
        self.companyname_showbox=self.login_page.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.myzone_menu=self.login_page.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.product_menu=self.login_page.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.username_showspan=self.login_page.driver.find_element(By.XPATH,'//span[@class="user-name"]')

    def get_companyname(self): #获取公司名称
        value=self.companyname_showbox.get_attribute('title')
        logutils.info('获取公司名称：%s'%value)
        return value

    def goto_myzone(self):#进入我的地盘菜单
        self.myzone_menu.click()
        logutils.info('进入我的地盘菜单')

    def goto_product(self):#进入产品菜单
        self.product_menu.click()
        logutils.info('进入产品页面菜单')

    def get_username(self):#获取用户名
        value=self.username_showspan.text
        logutils.info('获取登录用户名：%s'%value)
        return value


if __name__=='__main__':
    main_page=MainPage()
    companyname=main_page.get_companyname()
    print(companyname)
    username=main_page.get_username()
    print(username)
    #增加以下两句代码后出现了一个问题，
    #问题原因：
    #线性脚本 操作一个元素再去识别下一个元素
    #目前版本的PO模式，是实例化页面对象之后，识别所有的元素，然后再去操作，可能发生元素不能识别
    main_page.goto_myzone()
    main_page.goto_product()

