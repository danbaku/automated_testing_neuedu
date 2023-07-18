"""
作者：mrqc
时间：2023/7/17 15:57
"""

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://mail.qq.com/")

driver.implicitly_wait(15)

driver.maximize_window()

loc_frame = (By.XPATH,'//iframe[@CLASS="QQMailSdkTool_login_loginBox_qq_iframe"]')

ec = EC.frame_to_be_available_and_switch_to_it(loc_frame)

WebDriverWait(driver,20,0.5).until(ec)

loc_frame2 = (By.XPATH,'//iframe[@ID="ptlogin_iframe"]')

ec2 = EC.frame_to_be_available_and_switch_to_it(loc_frame2)

WebDriverWait(driver,20,0.5).until(ec2)

driver.find_element(by=By.LINK_TEXT,value="密码登录").click()

driver.find_element(by=By.ID, value="u").send_keys("2351674")

driver.find_element(by=By.ID, value="p").send_keys("88888888")

time.sleep(1)

driver.find_element(by=By.ID, value="login_button").click()

time.sleep(2)

loc_frame3 = (By.XPATH,'//iframe[@ID="tcaptcha_iframe_dy"]')

ec3 = EC.frame_to_be_available_and_switch_to_it(loc_frame3)

WebDriverWait(driver,20,0.5).until(ec3)

driver.implicitly_wait(20)

driver.find_element(By.XPATH,'//*[@id="tcOperation"]/div[6]').click()

time.sleep(5)

driver.close()