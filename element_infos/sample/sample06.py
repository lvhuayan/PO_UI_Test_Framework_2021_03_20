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
#测试base_page中window句柄封装是否正确

current_path=os.path.dirname(__file__)
page_path=os.path.join(current_path,'../../pages/element_samples.html')

class Sample06(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        elements=ElementDataUtils('sample06','sample06_page').get_element()
        self.select_menu=elements['select_menu']
        self.government_service_link=elements['government_service_link']

    def select_government(self,government_name):
        self.select_by_visible_text(self.select_menu,government_name)

    def click_government_service_link(self,nemu_name):
        self.government_service_link['locator_value']=self.government_service_link['locator_value']%nemu_name
        self.click(self.government_service_link)


if __name__=='__main__':
    sample06_page=Sample06(Browser().get_driver())
    sample06_page.open_url('file://'+page_path)
    sample06_page.implicitly_wait()
    sample06_page.set_browser_max()
    sample06_page.select_government('开封教育网')
    sample06_page.switch_to_handle_by_title('开封市教育体育局')
    # sample06_page.switch_to_handle_by_url('http://jtj.kaifeng.gov.cn/')
    sample06_page.click_government_service_link('政务服务')

