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
    def get_log_level(self):
        return int(self.read_ini('default','log_level'))

    @property
    def get_webdriver_path(self):
        return self.read_ini('default','webdriver_path')

    @property
    def get_driver_name(self):
        return self.read_ini('default','driver_name')

    @property
    def get_time_out(self):
        return float(self.read_ini('default','time_out'))

    @property
    def get_element_info_path(self):
        return self.read_ini('default','element_info_path')

    @property
    def get_screenshot_path(self):
        return self.read_ini('default','screenshot_path')

    @property
    def get_log_path(self):
        return self.read_ini('default','log_path')

    @property
    def get_username(self):
        return self.read_ini('default','username')

    @property
    def get_password(self):
        return self.read_ini('default','password')

    @property
    def get_url(self):
        return self.read_ini('default','url')

    @property
    def get_testdata_path(self):
        return self.read_ini('default','test_data_path')

    @property
    def get_case_path(self):
        return self.read_ini('default','case_path')

    @property
    def get_report_path(self):
        return self.read_ini('default','report_path')

    @property
    def get_smtp_server(self):
        return self.read_ini('email','smtp_server')

    @property
    def get_smtp_sender(self):
        return self.read_ini('email','smtp_sender')

    @property
    def get_smtp_senderpassword(self):
        return self.read_ini('email','smtp_senderpassword')

    @property
    def get_smtp_receiver(self):
        return self.read_ini('email','smtp_receiver')

    @property
    def get_smtp_cc(self):
        return self.read_ini('email','smtp_cc')

    @property
    def get_smtp_subject(self):
        return self.read_ini('email','smtp_subject')



Config=CongfigUtlis()

if __name__=='__main__':
    configutils=CongfigUtlis()
    print(configutils.get_element_info_path)