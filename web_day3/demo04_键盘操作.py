"""
作者：张浩
时间：2023/7/18  11:05
邮箱：88302599@qq.com
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.implicitly_wait(15)

driver.find_element(by=By.ID,value="kw").send_keys(Keys.CONTROL,Keys.SHIFT,Keys.DELETE)
driver.find_element(by=By.ID,value="kw").send_keys(Keys.ENTER)