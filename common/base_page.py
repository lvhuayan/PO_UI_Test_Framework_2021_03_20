#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: base_page.py
# @time: 2021/3/16 21:57
# @desc:
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from common.config_utils import Config
from common.log_utils import logutils

class BasePage:
    def __init__(self,driver):
        self.driver=driver  #webdriver.Chrome

    def open_url(self,url):
        self.driver.get(url)
        logutils.info('打开url地址:%s'%url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logutils.info('设置浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logutils.info('设置浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logutils.info('刷新浏览器')

    def get_title(self):
        value=self.driver.title
        logutils.info('获取网页标题，标题是%s'%value)
        return value

    def find_element(self,element_info):
        locator_type_name=element_info['locator_type']
        locator_value_info=element_info['locator_value']
        locator_timeout=element_info['timeout']
        if locator_type_name=='id':
            locator_type=By.ID
        elif locator_type_name=='xpath':
            locator_type=By.XPATH
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        element=WebDriverWait(self.driver,locator_timeout).until(lambda x:x.find_element(locator_type,locator_value_info))
        logutils.info('【%s】元素识别成功'%element_info['element_name'])
        return element

    def input(self,element_info,content):
        element=self.find_element(element_info)
        element.send_keys(content)
        logutils.info('【%s】元素输入内容：%s'%(element_info['element_name'],content))

    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()
        logutils.info('【%s】元素进行点击操作'%element_info['element_name'])


    #frame封装
    #思路一
    def switch_to_frame(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)

    # 思路二
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)

    #selenium执行js
    def execute_script(self,js_str,element_info=None):
        if element_info:
            self.driver.execute_script(js_str)
        else:
            self.driver.execute_script(js_str,None)

    #使用了了封装的execute_script()方法
    def __delete_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element)

    # 未使用封装的execute_script()方法
    def delete_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name, element)

    def update_element_attribute(self,element_info,attribute_name,attribute_value):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value), element)


    def implicitly_wait(self,seconds=Config.get_time_out):
        self.driver.implicitly_wait(seconds)

    def wait_time(self,seconds=Config.get_time_out):
        time.sleep(seconds)
