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

#测试base_page中select下拉框方法是否封装正确
current_path=os.path.dirname(__file__)
page_path=os.path.join(current_path,'../../pages/element_samples.html')

class Sample03(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements=ElementDataUtils('sample03','sample03_page').get_element()
        self.select_menu=elements['select_menu']


    def select_menu_value1(self,content):
        self.select_by_visible_text(self.select_menu,content)

    def select_menu_value2(self,content):
        self.select_by_value(self.select_menu,content)

    def select_menu_value3(self, content):
        self.select_by_index(self.select_menu, content)


if __name__=='__main__':
    sample03_page=Sample03(Browser().get_driver())
    sample03_page.set_browser_max()
    sample03_page.open_url('file://'+page_path)
    sample03_page.implicitly_wait()
    # sample03_page.select_menu_value1('香蕉')
    # sample03_page.select_menu_value2('peach')
    sample03_page.select_menu_value3(4)



