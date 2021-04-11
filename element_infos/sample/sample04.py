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

#测试base_page中 #selenium执行js方法是否封装正确
current_path=os.path.dirname(__file__)
page_path=os.path.join(current_path,'../../pages/element_samples.html')

class Sample04(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements=ElementDataUtils('sample04','sample04_page').get_element()
        self.show_select_result=elements['show_select_result']

    def delete_attribute(self,content):
        self.delete_element_attribute(self.show_select_result,content)

    def delete_attribute01(self, content):
         self.delete_element_attribute01(self.show_select_result, content)

    def execute_js1(self,js_str):
        self.execute_script(js_str,self.show_select_result)

    def execute_js2(self,js_str):
        self.execute_script(js_str)

    def update_attribute(self,attribute_name,attribute_value):
        self.update_element_attribute(self.show_select_result,attribute_name,attribute_value)



if __name__=='__main__':
    sample04_page=Sample04(Browser().get_driver())
    sample04_page.set_browser_max()
    sample04_page.open_url('file://'+page_path)
    sample04_page.implicitly_wait()
    # sample04_page.delete_attribute('value')
    sample04_page.delete_attribute01('value')

    # sample04_page.update_attribute('value','newdream')

    # js_str1= 'arguments[0].removeAttribute("value");'
    # sample04_page.execute_js1(js_str1)

    # js_str2='document.body.scrollTop=%d;'
    # sample04_page.execute_js2(js_str2%5000)




