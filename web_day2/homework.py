"""
作者：张浩
时间：2023/7/17  9:35
邮箱：88302599@qq.com
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(by=By.LINK_TEXT, value="登录").click()
time.sleep(10)
# driver.find_element(by=By.ID,value="TANGRAM__PSP_30__changePwdCodeItem").click()
#
# elm = driver.find_element(by=By.ID, value="TANGRAM__PSP_30__userName")
# print(elm)
#
# js = "arguments[0].value=arguments[1]"
# driver.execute_script(js,elm,"17768148441")

# elm.send_keys("17768148441")
#
# driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("17768148441")
#
#
# driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("17768148441")
#
# driver.find_element(by=By.ID, value="TANGRAM__PSP_1__submit").click()
