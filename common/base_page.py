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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from common.config_utils import Config
from common.log_utils import logutils

current_path=os.path.dirname(__file__)

class BasePage:
    def __init__(self,driver):
        self.driver=webdriver.Chrome()   #webdriver.Chrome()  driver

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

    def close_tab(self):
        self.driver.close()
        logutils.info('关闭当前tab页')

    def quit_browser(self):
        self.driver.quit()
        logutils.info('关闭浏览器')

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

    def get_text(self,element_info):#获取属性的文本
        element=self.find_element(element_info)
        text_value=element.text
        logutils.info('获取【%s】的属性值：%s'%(element_info['element_name'],text_value))
        return text_value

    #下拉框封装
    def select_by_value(self,element_info,content):
        element =self.find_element(element_info)
        select_el = Select(element)
        select_el.select_by_value(content)  # value属性的值
        logutils.info('【%s】元素根据value属性值：%s获取下拉框选项值'%(element_info['element_name'],content))

    def select_by_visible_text(self, element_info, content):
        element = self.find_element(element_info)
        select_el = Select(element)
        select_el.select_by_visible_text(content)  # 可见文本内容
        logutils.info('【%s】元素根据可见文本内容：%s获取下拉框选项值'%(element_info['element_name'],content))

    def select_by_index(self, element_info, content):
        element = self.find_element(element_info)
        select_el = Select(element)
        select_el.select_by_index(content)  # 索引定位，索引从0开始
        logutils.info('【%s】元素根据索引：%s获取下拉框选项值'%(element_info['element_name'],content))

    #frame封装
    #思路一
    def switch_to_frame(self,element_info):
        element=self.find_element(element_info)
        self.driver.switch_to.frame(element)
        logutils.info('根据元素信息切换到frame中')

    # 思路二
    def switch_to_frame_id_or_name(self,id_or_name):
        self.driver.switch_to.frame(id_or_name)
        logutils.info('根据id或者name切换到frame中')

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        logutils.info('将识别的主体切换出frame')

    #鼠标键盘封装
    def move_to_element_by_mouse(self,element_info):
        element = self.find_element(element_info)
        ActionChains(self.driver).move_to_element(element).perform()
        logutils.info('鼠标移动到元素【%s】上'%element_info['element_name'])

    def long_press_element(self,element_info,seconds):
        element = self.find_element(element_info)
        ActionChains(self.driver).click_and_hold(element).pause(seconds).release(element).perform()
        logutils.info('鼠标长按【%s】元素%s秒' % (element_info['element_name'],seconds))

    #弹出窗封装
    def switch_to_alert(self,action='accept',time_out=Config.get_time_out):
        WebDriverWait(self.driver,time_out).until(EC.alert_is_present())
        alert=self.driver.switch_to.alert
        alert_text=alert.text
        if action=='accept':
            alert.accept()
        elif action=='dismiss':
            alert.dismiss()
        logutils.info('切换到alert弹窗并完成了操作')
        return alert_text

    #window句柄封装
    #此方法没测试
    def get_current_handle(self):
        self.driver.current_window_handle
        logutils.info('获取当前页面句柄')

    # 此方法没测试
    def switch_to_handle_by_handle(self, window_handle):
        self.driver.switch_to.window(window_handle)
        logutils.info('根据句柄切换')

    def switch_to_handle_by_title(self,title):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            self.driver.switch_to.window(window_handle)
            if self.driver.title.__contains__(title):
                break
            logutils.info('根据title:%s切换句柄' % title)

    #此方法没有验证通过
    # def switch_to_handle_by_title(self,title):
    #     window_handles=self.driver.window_handles
    #     for window_handle in window_handles:
    #         if WebDriverWait(self.driver,Config.get_time_out).until(EC.title_contains(title)):
    #             self.driver.switch_to.window(window_handle)
    #             break

    def switch_to_handle_by_url(self,url):
        window_handles=self.driver.window_handles
        for window_handle in window_handles:
            self.driver.switch_to.window(window_handle)
            if self.driver.title.__contains__(url):
                break
        logutils.info('根据url切换句柄')

    #截图功能封装
    def screenshot_as_file(self,*screenshot_path):
        if(len(screenshot_path)==0):
            screenshotfile_path=Config.get_screenshot_path
        else:
            screenshotfile_path=screenshot_path[0]
        now=time.strftime('%Y-%m-%d-%H-%M-%S')
        screenshotfile_path=os.path.join(current_path,'..',screenshotfile_path,'UITest_%s.png'%now)
        self.driver.get_screenshot_as_file(screenshotfile_path)
        logutils.info('截图成功，图片地址在：%s'%screenshotfile_path)

    #selenium执行js
    def execute_script(self,js_str,element_info=None):
        if element_info:
            element = self.find_element(element_info)
            self.driver.execute_script(js_str,element)
            logutils.info('在【%s】元素上执行js:%s'%(element_info['element_name'],js_str))
        else:
            self.driver.execute_script(js_str,None)
            logutils.info('执行js:%s' %js_str)


    #使用了封装的execute_script()方法
    def delete_element_attribute01(self,element_info,attribute_name):
        self.execute_script('arguments[0].removeAttribute("%s");'%attribute_name,element_info)

    # 未使用封装的execute_script()方法
    def delete_element_attribute(self,element_info,attribute_name):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].removeAttribute("%s");'%attribute_name, element)
        logutils.info('删除【%s】元素的%s属性'%(element_info['element_name'],attribute_name))

    def update_element_attribute(self,element_info,attribute_name,attribute_value):
        element=self.find_element(element_info)
        self.driver.execute_script('arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_value), element)
        logutils.info('修改【%s】元素的%s属性值为：%s:'%(element_info['element_name'],attribute_name,attribute_value))


    def implicitly_wait(self,seconds=Config.get_time_out):
        self.driver.implicitly_wait(seconds)
        logutils.info('隐式等待%s秒'%seconds)


    def wait_time(self,seconds=Config.get_time_out):
        time.sleep(seconds)
        logutils.info('固定等待%s秒' % seconds)
