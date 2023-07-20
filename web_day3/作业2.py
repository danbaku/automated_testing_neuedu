"""
作者：mrqc
时间：2023/7/18 19:15
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from pywinauto.keyboard import send_keys

driver = webdriver.Chrome()

driver.get("https://layui.dev/docs/2.8/upload/")

driver.maximize_window()

driver.implicitly_wait(15)

driver.find_element(by=By.XPATH, value='//button[contains(@lay-options,"zip|rar|7z")]').click()

time.sleep(2)

send_keys(r'"E:\个人\实训\三年级第二次实训\web_day3\材料包\test1.zip"')

time.sleep(2)

send_keys("{VK_RETURN}")

time.sleep(3)

driver.close()