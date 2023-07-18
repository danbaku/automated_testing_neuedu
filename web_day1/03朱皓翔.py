"""
作者：mrqc
时间：2023/7/16 16:06
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

driver.find_element(by=By.LINK_TEXT, value="登录").click()

time.sleep(2)

driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys("13405879612")

driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("rW6$cG1:mW")

driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()

time.sleep(5)

driver.close()