import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.log_utils import logutils

current_path=os.path.dirname(__file__)
driver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')

class LoginPage:
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.username_inputbox=self.driver.find_element(By.XPATH,'//input[@id="account"]') #属性==》页面的控件
        self.password_inputbox=self.driver.find_element(By.XPATH,'//input[@name="password"]')
        self.login_button=self.driver.find_element(By.XPATH,'//button[@id="submit"]')

    def input_username(self,username): #输入用户名  #方法==》控件的操作
        self.username_inputbox.send_keys(username)
        logutils.info('用户名输入框输入%s：'%username)

    def input_password(self,password):#输入密码
        self.password_inputbox.send_keys(password)
        logutils.info('密码输入框输入了：%s'%password)

    def click_login(self):#点击登录
        self.login_button.click()
        logutils.info('点击登录按钮')

if __name__=='__main__':
    login_page=LoginPage()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()