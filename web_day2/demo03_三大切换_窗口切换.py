"""
作者：张浩
时间：2023/7/17  13:34
邮箱：88302599@qq.com
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("http://www.qq.com")
driver.implicitly_wait(15)
driver.maximize_window()


before_handler = driver.window_handles
print(before_handler)
driver.find_element(by=By.LINK_TEXT,value="新闻").click()

#等待新页面生成
ec = EC.new_window_is_opened(before_handler)
WebDriverWait(driver,20,0.5).until(ec)

after_handler = driver.window_handles
print(after_handler)

driver.switch_to.window(after_handler[-1])#通过新页面的句柄切换新页面

driver.find_element(by=By.LINK_TEXT,value="江苏").click()
