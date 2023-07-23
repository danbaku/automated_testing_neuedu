"""
作者：张浩
时间：2023/7/20  14:31
邮箱：88302599@qq.com
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittestreport import ddt,list_data

testcase=[
    {"data":{"user":"","passwd":"2620075Zh"},"expect":"请您输入手机号/用户名/邮箱"},
    {"data":{"user":"17768148441","passwd":""},"expect":"请您输入密码"},
    {"data":{"user":"17768148441","passwd":"1234567"},"expect":"找回密码"},
    {"data":{"user":"177681484412奥术大师大所多","passwd":"2620075Zh"},"expect":"您输入的帐号格式不正确"}
]


@ddt
class Test_Baidu_Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.driver.find_element(by=By.LINK_TEXT, value="登录").click()

    def test_login_succ(self):

        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys("17768148441")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("2620075Zh")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()

        time.sleep(3)

        # elm = driver.find_element(by= By.XPATH,value='//span[@class="user-name c-font-normal c-color-t"]')

        res = self.driver.find_element(by=By.XPATH, value='//span[@class="user-name c-font-normal c-color-t"]').text

        assert res == "浩Legend"

    @list_data(testcase)
    def test_login_fail(self,item):
        #1、准备数据
        user = item["data"]["user"]
        pwd = item["data"]["passwd"]
        expect = item["expect"]

        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys(user)
        self.driver.find_element(by=By.ID,value="TANGRAM__PSP_11__password").send_keys(pwd)
        self.driver.find_element(by=By.ID,value="TANGRAM__PSP_11__submit").click()

        time.sleep(3)

        res = self.driver.find_element(by = By.ID,value="TANGRAM__PSP_11__error").text

        assert res ==expect



