"""
作者：mrqc
时间：2023/7/17 15:57
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://kf.qq.com/product/weixin.html")

driver.find_element(by=By.LINK_TEXT, value="手机版微信").click()

driver.implicitly_wait(15)

driver.find_element(by=By.LINK_TEXT, value="微信群").click()

driver.implicitly_wait(15)

driver.find_element(by=By.LINK_TEXT, value="微信群创建及设置方法").click()

time.sleep(5)

driver.close()