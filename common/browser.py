#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: browser.py
# @time: 2021/3/19 21:56
# @desc:
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.config_utils import Config
from common.log_utils import logger

current_path = os.path.dirname(__file__)
dri_path = os.path.join(current_path, '..',Config.get_webdriver_path)
dri_name=Config.get_driver_name

class Browser:
    def __init__(self,driver_path=dri_path,driver_name=dri_name):
        self.__driver_path=driver_path
        self.__driver_name=driver_name

    def get_driver(self):
        if self.__driver_name.lower()=='chrome':
            return self.__get_chrome_driver()
        elif self.__driver_name.lower()=='firefox':
            return self.__get_firefox_driver()
        elif self.__driver_name.lower()=='edge':
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        chrome_options=Options()
        chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8') #设置默认编码为UTF-8
        chrome_options.add_experimental_option('useAutomationExtension', False)# 屏蔽谷歌浏览器正在接收自动化软件控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])# 屏蔽谷歌浏览器正在接收自动化软件控制提示
        chrome_driver_path=os.path.join(self.__driver_path,'chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_path)
        logger.info('初始化并启动谷歌浏览器')
        return driver

    def __get_firefox_driver(self):
        firefox_driver_path=os.path.join(self.__driver_path,'geckodriver.exe')
        driver = webdriver.Chrome(executable_path=firefox_driver_path)
        logger.info('初始化并启动火狐浏览器')
        return driver

    def __get_edge_driver(self):
        edge_driver_path=os.path.join(self.__driver_path,'MicrosoftWebDriver.exe')
        driver = webdriver.Chrome(executable_path=edge_driver_path)
        logger.info('初始化并启微软浏览器')
        return driver

    def __get_remote_driver(self):#selenium支持分布式grid ==》配置（你自己的代码编写、配置）
        pass

if __name__=='__main__':
    Browser().get_chrome_driver()