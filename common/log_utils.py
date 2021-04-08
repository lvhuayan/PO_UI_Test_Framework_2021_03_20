#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: log_utilds.py
# @time: 2021/2/10 21:30
# @desc:
import os
import logging
import time

from common.config_utils import Config

current_path=os.path.dirname(__file__)
log_path=os.path.join(current_path,'..',Config.get_log_path)

class LogUtils:
    def __init__(self,logger=None):
        self.log_name=os.path.join(log_path,'UITest_%s.log'%time.strftime('%Y_%m_%d'))
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(Config.get_log_level)

        self.fh=logging.FileHandler(self.log_name,'a',encoding='utf-8')
        self.fh.setLevel(Config.get_log_level)
        self.sh=logging.StreamHandler()
        self.sh.setLevel(Config.get_log_level)
        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s')
        self.fh.setFormatter(formatter)
        self.sh.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.sh)
        self.fh.close()
        self.sh.close()

    def get_log(self):
        return  self.logger

    # def info(self,message):
    #     self.logger.info(message)
    #
    # def error(self,message):
    #     self.logger.error(message)

logger=LogUtils().get_log()

if __name__=='__main__':
    logger.info('hello')

