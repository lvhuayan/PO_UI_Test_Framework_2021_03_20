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

#测试base_page中switch_to_frame方法是否封装正确
current_path=os.path.dirname(__file__)
page_path=os.path.join(current_path,'../../pages/main.html')

class Sample02(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements=ElementDataUtils('sample02','sample02_page').get_element()
        self.frame_xpath=elements['frame_xpath']
        self.input01_inputbox=elements['input01_inputbox']
        self.input02_inputbox=elements['input02_inputbox']
        self.span_text=elements['span_text']

    def frame_info(self):
        self.switch_to_frame(self.frame_xpath)

    def input_text01(self,content):
        self.input(self.input01_inputbox,content)

    def input_text02(self,content):
        self.input(self.input02_inputbox,content)

    def get_span_text(self):
        self.get_text(self.span_text)

if __name__=='__main__':
    sample02_page=Sample02(Browser().get_driver())
    sample02_page.open_url('file://'+page_path)
    sample02_page.implicitly_wait()
    sample02_page.frame_info()
    # sample02_page.switch_to_frame_id_or_name('frame１')
    sample02_page.input_text01('newdream')
    sample02_page.input_text02('test')
    sample02_page.switch_to_default_content()
    sample02_page.get_span_text()


