"""
作者：mrqc
时间：2023/7/18 16:17
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.ketangpai.com/#/login")

driver.maximize_window()

driver.implicitly_wait(15)

driver.find_elements(by=By.CLASS_NAME, value="el-input__inner")[0].send_keys("13405879612")

driver.find_elements(by=By.CLASS_NAME, value="el-input__inner")[1].send_keys("rE8~fP3-aM")

driver.implicitly_wait(15)

log = driver.find_element(by=By.XPATH, value='//button[@class="el-button el-button--primary el-button--medium"]')

js = "arguments[0].click();"

driver.execute_script(js,log)

time.sleep(3)

driver.close()