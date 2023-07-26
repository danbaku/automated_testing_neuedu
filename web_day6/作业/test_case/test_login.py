import time
import unittest
from unittestreport import ddt, list_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from add_data import add_test_data

# 从Excel文件中读取测试数据
test_data = add_test_data(r'D:\桌面\123\fire_project\fire_project\fire_data.xlsx', "test_data")

@ddt
class TestBaiduLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(r"D:\桌面\123\fire_project\fire_project\log_on\html.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        time.sleep(1)
        # 点击切换账号按钮
        self.driver.find_element(by=By.XPATH, value='//div[@id="switch-c1"]//button').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    # 点击登录按钮
    def login_on(self):
        self.driver.find_element(by=By.ID, value="login").click()
        time.sleep(1)

    @list_data(test_data)
    def test_login_email(self, item):
        # 输入用户名和密码
        self.driver.find_element(by=By.ID, value="name").send_keys(item["data"]["user_name"])
        self.driver.find_element(by=By.ID, value="pass").send_keys(item["data"]["passwd"])
        self.login_on()  # 调用登录函数
        alert_data = self.driver.switch_to.alert.text  # 获取弹窗的文本
        self.driver.switch_to.alert.accept()
        expect = item["expect"]
        self.assertEqual(alert_data, expect)