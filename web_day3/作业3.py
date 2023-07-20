"""
作者：mrqc
时间：2023/7/18 20:34
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://layui.dev/docs/2.8/form/#examples")

driver.maximize_window()

driver.implicitly_wait(15)

time.sleep(2)

driver.find_element(by=By.XPATH, value='//label[text()="单行选择框"]/../div').click()

driver.find_element(by=By.XPATH, value='//label[text()="单行选择框"]/..//dd[text()="写作"]').click()

driver.find_element(by=By.XPATH, value="//input[@placeholder='请选择问题']").click()

driver.find_element(by=By.XPATH, value="//dd[@lay-value='你工作的第一个城市']").click()

driver.find_element(by=By.XPATH, value="//input[@placeholder='直接选择或搜索选择']").click()

driver.find_element(by=By.XPATH, value="//dd[contains(text(),'form')]").click()

driver.find_element(by=By.XPATH, value="//input[@value='浙江省']").click()

driver.find_element(by=By.XPATH, value="//input[@placeholder='请选择市']").click()

driver.find_element(by=By.XPATH, value="//dd[contains(text(),'台州')]").click()

driver.find_element(by=By.XPATH, value="//input[@placeholder='请选择县/区']").click()

driver.find_element(by=By.XPATH, value='//dd[@lay-value="拱墅区"]').click()

# time.sleep(3)
#
# driver.close()