#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: excel_utils.py
# @time: 2021/4/4 11:14
# @desc:
import os
import xlrd

from common.config_utils import Config

current_path=os.path.dirname(__file__)
excel_file_path=os.path.join(current_path,'../element_info_datas/element_infos.xls')

class ExcelUtils:
    """
    判断是否是excel文件再处理xls|xlsx 并且文件存在
    """
    def __init__(self,sheet_name=None,excel_path=excel_file_path):
        self.sheet_name=sheet_name
        self.excel_path=excel_path
        self.sheet_data=self.__get_sheet_data()

    def __get_sheet_data(self):#当没带参数时 默认取第一个表格
        workbook= xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet=workbook.sheet_by_name(self.sheet_name)
        else:
            sheet=workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        row_count=self.sheet_data.nrows
        return row_count

    @property
    def get_clo_count(self):
        clo_count=self.sheet_data.ncols
        return clo_count

    def get_excel_data_by_list(self): #把excel数据通过列表返回[[],[],[]...]
        all_excel_data=[]
        for row_num in range(self.get_row_count):
            row_excel_data=[]
            for clo_num in range(self.get_clo_count):
                cell_value=self.sheet_data.cell_value(row_num,clo_num)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data

if __name__=='__main__':
    # excl_utils=ExcelUtils('main')
    # print(excl_utils.get_clo_count)
    # print(excl_utils.get_row_count)
    # data=excl_utils.get_excel_data_by_list()
    # print(data)

    current_path = os.path.dirname(__file__)
    testdata_path = os.path.join(current_path,'..', Config.get_testdata_path)
    excel_data = ExcelUtils('login_suite', testdata_path).get_excel_data_by_list()
    print(excel_data)










