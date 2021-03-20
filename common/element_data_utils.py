#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: element_data_utils.py
# @time: 2021/3/17 15:34
# @desc:
import os
import xlrd

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/element_infos.xls')

class ElementDataUtils:
    def __init__(self,page_name,element_path=excel_path):
        self.workbook = xlrd.open_workbook(excel_path)
        self.sheet = self.workbook.sheet_by_name(page_name)
        self.nrow = self.sheet.nrows

    def get_element(self):
        element_infos = {}
        for i in range(1, self.nrow):
            element_info = {}
            element_info['element_name'] = self.sheet.cell_value(i, 1)
            element_info['locator_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)
            element_info['timeout'] =self.sheet.cell_value(i, 4)
            element_infos[self.sheet.cell_value(i, 0)] = element_info
        return element_infos

if __name__=='__main__':
    elements=ElementDataUtils('login_page').get_element()
    print(elements)
