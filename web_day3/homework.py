"""
作者：张浩
时间：2023/7/18  9:22
邮箱：88302599@qq.com
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#-------------------第一题--------------------------
# driver = webdriver.Chrome()
# driver.get("https://kf.qq.com/product/weixin.html")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
#
# driver.find_element(by=By.ID,value="m_1453").click()
#
# loc_weixin = (By.ID,"1463")
#
# ec = EC.presence_of_element_located(loc_weixin)
# WebDriverWait(driver,20,0.5).until(ec)
#
# #*loc_weixin作用叫拆包
# driver.find_element(*loc_weixin).click()
#
# loc_fun = (By.LINK_TEXT,"微信群创建及设置方法")
#
# ec = EC.presence_of_element_located(loc_fun)
# WebDriverWait(driver,20,0.5).until(ec)
#
# driver.find_element(*loc_fun).click()
#
# time.sleep(5)
# driver.close()

#-------------------第二题--------------------------

driver = webdriver.Chrome()
driver.get("https://mail.qq.com")
driver.maximize_window()
driver.implicitly_wait(15)

frame_1=(By.XPATH,'//iframe[@class="QQMailSdkTool_login_loginBox_qq_iframe"]')
ec = EC.frame_to_be_available_and_switch_to_it(frame_1)
WebDriverWait(driver,20,0.5).until(ec)


frame_2 = (By.ID,"ptlogin_iframe")
ec = EC.frame_to_be_available_and_switch_to_it(frame_2)
WebDriverWait(driver,20,0.5).until(ec)



driver.find_element(by=By.ID,value='switcher_plogin').click()

driver.find_element(by=By.ID,value="u").send_keys("17768148441")
driver.find_element(by=By.ID,value="p").send_keys("17768148441")

driver.find_element(by=By.ID,value="login_button").click()
time.sleep(3)

driver.switch_to.default_content()#返回最外层
driver.switch_to.parent_frame()#返回上一层

frame_1=(By.XPATH,'//iframe[@class="QQMailSdkTool_login_loginBox_qq_iframe"]')
ec = EC.frame_to_be_available_and_switch_to_it(frame_1)
WebDriverWait(driver,20,0.5).until(ec)


frame_2 = (By.ID,"ptlogin_iframe")
ec = EC.frame_to_be_available_and_switch_to_it(frame_2)
WebDriverWait(driver,20,0.5).until(ec)


# frame_3=driver.find_element(by=By.ID,value="tcaptcha_iframe_dy")
#
# print(frame_3)
# driver.switch_to.frame(frame_3)
#
frame_3 = (By.XPATH,'//iframe[@id="tcaptcha_iframe_dy"]')
ec = EC.frame_to_be_available_and_switch_to_it(frame_3)
WebDriverWait(driver,20,0.5).until(ec)

time.sleep(3)
#
#
elm_div=driver.find_element(by=By.XPATH,value='//*[@id="tcOperation"]/div[6]')
#
print(elm_div)