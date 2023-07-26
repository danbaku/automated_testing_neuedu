import time
import unittest

from unittestreport import ddt,list_data
from selenium import webdriver
from selenium.webdriver.common.by import By


test_case=[
    {"data":{"username":"","password":"rE8~fP3-aM"},"expect_data":"用户名不能为空"},
    {"data":{"username":"13405879612","password":"rE8~f"},"expect_data":"密码有效长度是6到30个字符"},
    {"data":{"username":"1340587961","password":"rE8~fP3-aM"},"expect_data":"用户不存在"}
]




@ddt
class Test_Pai_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(r"https://www.ketangpai.com/#/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(1)

    #点击登录按钮
    def click_button(self):
        log = self.driver.find_element(by=By.XPATH,value='//button[@class="el-button el-button--primary el-button--medium"]')
        js = "arguments[0].click();"
        self.driver.execute_script(js, log)

    @list_data(test_case)
    def test_login_other_error(self,item):
        self.driver.find_element(by=By.XPATH,value="//input[@placeholder='请输入邮箱/手机号/账号']").send_keys(item["data"]["username"])              #输入用户名
        self.driver.find_element(by=By.XPATH, value="//input[@placeholder='请输入密码']").send_keys(item["data"]["password"])             #输入密码
        time.sleep(1)
        self.click_button()                         #调用函数
        time.sleep(1)
        expect_text=self.driver.find_element(by=By.XPATH, value="//div[@role='alert']//p").text                     #实际结果
        time.sleep(1)
        res = item["expect_data"]
        print("报错文本" + expect_text)
        print("预期结果" + res)
        assert expect_text == res