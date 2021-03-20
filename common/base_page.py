#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: base_page.py
# @time: 2021/3/16 21:57
# @desc:
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.log_utils import logutils

class BasePage:
    def __init__(self,driver):
        self.driver=driver

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