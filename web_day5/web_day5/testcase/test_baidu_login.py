"""
作者：张浩
时间：2023/7/20  14:31
邮箱：88302599@qq.com
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


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


    def test_login_fail_unull(self):


        self.driver.find_element(by=By.ID,value="TANGRAM__PSP_11__userName").send_keys("")
        self.driver.find_element(by=By.ID,value="TANGRAM__PSP_11__password").send_keys("2620075Zh")
        self.driver.find_element(by=By.ID,value="TANGRAM__PSP_11__submit").click()

        time.sleep(3)

        res = self.driver.find_element(by = By.ID,value="TANGRAM__PSP_11__error").text

        assert res == "请您输入手机号/用户名/邮箱"

    def test_login_fail_pnull(self):


        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys("17768148441")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()

        res = self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__error").text

        assert res == "请您输入密码"

    def test_login_fail_perr(self):


        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys("17768148441")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("1234567")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()

        time.sleep(2)
        res = self.driver.find_element(by=By.XPATH, value='//a[@href="http://passport.baidu.com/?getpassindex&account=17768148441&tpl=mn&u=https://www.baidu.com/"]').text


        assert res == "找回密码"

    def test_login_fail_uforamt(self):


        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys("177681484412奥术大师大所多")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("2620075Zh")
        self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()
        time.sleep(5)
        res = self.driver.find_element(by=By.ID, value="TANGRAM__PSP_11__error").text

        assert res == "您输入的帐号格式不正确"