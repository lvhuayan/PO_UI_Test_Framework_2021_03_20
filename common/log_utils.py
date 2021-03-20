#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: log_utilds.py
# @time: 2021/2/10 21:30
# @desc:
import os
import logging

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'../logs/test.log')

class LogUtils:
    def __init__(self,logfile_path=log_path):
        self.logfile_path=logfile_path
        self.logger=logging.getLogger('my_log')
        self.logger.setLevel(level=logging.INFO)
        self.file_log=logging.FileHandler(self.logfile_path)
        fomatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        self.file_log.setFormatter(fomatter)
        self.logger.addHandler(self.file_log)

    def info(self,message):
        self.logger.info(message)

    def error(self,message):
        self.logger.error(message)
logutils=LogUtils()

if __name__=='__main__':
    logutils=LogUtils()
    logutils.info('hello')

