"""
作者：张浩
时间：2023/7/17  14:44
邮箱：88302599@qq.com
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get(r"E:\class_2017\web_day2\test.html")
driver.implicitly_wait(15)
driver.maximize_window()


#------------------------一个按钮的弹框---------------------------------
# driver.find_element(by=By.XPATH,value='//button[text()="警告框"]').click()
#
# alert1=driver.switch_to.alert
# alert_text= alert1.text
# print(alert_text)
# time.sleep(3)
# alert1.accept()

#---------------------------两个按钮的弹框----------------------------------
# driver.find_element(by=By.XPATH,value='//button[text()="确认框"]').click()
# alert1=driver.switch_to.alert
# # alert1.accept()
# alert1.dismiss()


#--------------------------有输入框的弹框----------------------------
driver.find_element(by=By.XPATH,value='//button[text()="提示框"]').click()
alert1=driver.switch_to.alert

alert1.send_keys("AutoTest")
alert1.accept()
# alert1.dismiss()