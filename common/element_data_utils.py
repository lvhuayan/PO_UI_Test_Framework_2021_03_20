#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: element_data_utils.py
# @time: 2021/3/17 15:34
# @desc:
import os
import xlrd
from common.config_utils import Config

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'..',Config.get_element_info_path)

class ElementDataUtils:
    def __init__(self,modul_name,page_name,element_path=excel_path):
        self.element_path=element_path
        self.excel_path=os.path.join(self.element_path,modul_name,page_name+'.xls')
        self.workbook = xlrd.open_workbook(self.excel_path)
        self.sheet = self.workbook.sheet_by_index(0)
        self.nrow = self.sheet.nrows

    def get_element(self):
        element_infos = {}
        for i in range(1, self.nrow):
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i, 1)
            element_info['locator_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)
            time_out_value=self.sheet.cell_value(i, 4)
            #判断从excel中取出的超时时间是不是浮点型，是的话 直接取，不是浮点型数据则从配置文件中取值
            element_info['timeout'] =time_out_value if isinstance(time_out_value,float) else Config.get_time_out
            element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__=='__main__':
    elements=ElementDataUtils('login','login_page').get_element()
    print(elements)
