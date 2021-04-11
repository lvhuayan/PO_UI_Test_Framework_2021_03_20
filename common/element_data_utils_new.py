#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: element_data_utils.py
# @time: 2021/3/17 15:34
# @desc:
import os
import xlrd
from common.config_utils import Config
from common.excel_utils import ExcelUtils

# current_path=os.path.dirname(__file__)
# excel_path=os.path.join(current_path,'../element_info_datas/element_infos.xls')

#老师没有详细写 这是我自己写的
class ElementDataUtils:
    def __init__(self,modul_name,page_name,element_path=None):
        excl_utils = ExcelUtils(modul_name)
        self.element_path=excl_utils.excel_path
        self.page_name=page_name
        self.sheet =excl_utils.sheet_data
        self.nrow = excl_utils.get_row_count

    def get_element(self):
        element_infos = {}
        for i in range(1, self.nrow):
            if self.sheet.cell_value(i, 2)==self.page_name:
                element_info = {}
                element_info['element_name'] = self.sheet.cell_value(i, 1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                time_out_value=self.sheet.cell_value(i, 5)
                #判断从excel中取出的超时时间是不是浮点型，是的话 直接取，不是浮点型数据则从配置文件中取值
                element_info['timeout'] =time_out_value if isinstance(time_out_value,float) else Config.get_time_out
                element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__=='__main__':
    elements=ElementDataUtils('login','login_page').get_element()
    print(elements)
