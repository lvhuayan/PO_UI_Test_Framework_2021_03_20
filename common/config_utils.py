#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: config_utils.py
# @time: 2021/2/10 16:14
# @desc:
import os
import configparser

current_path=os.path.dirname(__file__)
cfgpath=os.path.join(current_path,'../conf/config.ini')
class CongfigUtlis():
    def __init__(self,conf_path=cfgpath):
        self.__conf=configparser.ConfigParser()
        self.__conf_data=self.__conf.read(conf_path,encoding='utf-8')

    def read_ini(self,sec,opt):
        value=self.__conf.get(sec,opt)
        return value
    @property
    def get_excel_path(self):
        return self.read_ini('default','excel_path')

    @property
    def get_log_path(self):
        return self.read_ini('default','log_path')

    @property
    def get_webdriver_path(self):
        return self.read_ini('default','webdriver_path')

    @property
    def get_driver_name(self):
        return self.read_ini('default','driver_name')

    @property
    def get_time_out(self):
        return float(self.read_ini('default','time_out'))

Config=CongfigUtlis()

if __name__=='__main__':
    configutils=CongfigUtlis()
    print(configutils.get_webdriver_path)