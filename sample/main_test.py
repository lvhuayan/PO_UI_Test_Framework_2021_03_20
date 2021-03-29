#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: main_test.py
# @time: 2021/3/27 17:41
# @desc:
from actions.login_action import LoginAction
from common.browser import Browser


driver = Browser().get_driver()
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
driver.maximize_window()
driver.implicitly_wait(5)
main_page = LoginAction(driver).login_sucessful('test01', 'newdream123')
driver.implicitly_wait(5)
value = main_page.get_username()
print(value)