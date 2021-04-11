#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: test_data_utils.py
# @time: 2021/4/9 18:14
# @desc:
import os
from common.excel_utils import ExcelUtils
from common.config_utils import Config

current_path=os.path.dirname(__file__)
testdata_path=os.path.join(current_path,'..',Config.get_testdata_path)

class TestDataUtils:
    def __init__(self,test_suite_name,test_file_name,test_class_name,test_data_path=testdata_path):
        self.test_data_path=os.path.join(test_data_path,test_suite_name,test_file_name+'.xls')
        self.test_class_name=test_class_name
        self.excel_data=ExcelUtils(test_class_name,self.test_data_path).get_excel_data_by_list()
        self.excel_rows=len(self.excel_data)

    def conver_exceldata_to_testdata(self):
        # {'test_login_sucess':
        #      {'testName':'验证正确的用户名密码能否成功登录',
        #       'testClass':'LoginTest',
        #       'isNot':'是',
        #       'expectResult':'测试人员1',
        #       'message':'test_login_success执行失败',
        #       'test_parameter':{'username':'test01','password':'newdream123'}
        #       },
        #  'test_login_fail':{}
        #  }
        test_data_infos={}
        for i in range(1,self.excel_rows):
            test_data_info = {}
            test_data_info['testName']=self.excel_data[i][1]
            test_data_info['isNot']=False if self.excel_data[i][2]=='是' else True
            test_data_info['expectResult']=self.excel_data[i][3]
            test_data_info['message']=self.excel_data[i][4]
            test_parameter = {}
            for j in range(5,len(self.excel_data[i])):
                if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j])>2:
                    parameter_info=self.excel_data[i][j].split('=')
                    test_parameter[parameter_info[0]]=parameter_info[1]
            test_data_info['test_parameter']=test_parameter
            test_data_infos[self.excel_data[i][0]]=test_data_info
        return test_data_infos


if __name__=='__main__':
    infos=TestDataUtils('login_suite','login_test','LoginTest').conver_exceldata_to_testdata()
    for i in infos.values():
        print(i)







