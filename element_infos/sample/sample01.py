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
#测试base_page中switch_to_alert方法是否封装正确

current_path=os.path.dirname(__file__)
page_path=os.path.join(current_path,'../../pages/element_samples.html')

class Sample01(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements=ElementDataUtils('sample01','sample01_page').get_element()
        self.button_toalert=elements['button_toalert']

    def click_alert_button(self):#点击测试alert弹框按钮
        self.click(self.button_toalert)

if __name__=='__main__':
    sample01_page=Sample01(Browser().get_driver())
    sample01_page.open_url('file://'+page_path)
    sample01_page.implicitly_wait()
    sample01_page.click_alert_button()
    sample01_page.switch_to_alert()
