"""
作者：张浩
时间：2023/7/19  9:15
邮箱：88302599@qq.com
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pywinauto.keyboard import send_keys
#------------------------课堂派登录--------------------------
# driver = webdriver.Chrome()
# driver.get("https://www.ketangpai.com/#/login")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
# driver.find_element(by=By.XPATH,value='//input[@placeholder="请输入邮箱/手机号/账号"]').send_keys("17768148441")
# driver.find_element(by=By.XPATH,value='//input[@placeholder="请输入密码"]').send_keys("2620075zh")
# btn=driver.find_element(by=By.XPATH,value='//button[@class="el-button el-button--primary el-button--medium"]')
#
# js = 'arguments[0].click();'
#
# driver.execute_script(js,btn)

#-----------------------上传-------------------------------

# driver = webdriver.Chrome()
# driver.get("https://layui.dev/docs/2.8/upload/")
# driver.maximize_window()
# driver.implicitly_wait(15)
#
#
# elm = driver.find_element(by=By.ID,value="ID-upload-demo-files-action")
#
# elm.location_once_scrolled_into_view
# #
# # driver.find_element(by=By.XPATH,value='//button[contains(@lay-options,"zip|rar|7z")]/../input[2]').send_keys(r"C:\Users\zhanghao\Desktop\11.rar")
#
# btn = driver.find_element(by=By.XPATH,value='//button[contains(@lay-options,"zip|rar|7z")]')
# btn.click()
#
# time.sleep(5)
#
# send_keys(r"C:\Users\zhanghao\Desktop\11.rar")
# send_keys("{VK_RETURN}")


#--------------------------------------------------------------------
driver = webdriver.Chrome()
driver.get("https://layui.dev/docs/2.8/form/")
driver.maximize_window()
driver.implicitly_wait(15)


driver.find_element(by=By.XPATH,value='//label[text()="单行选择框"]/..//input').click()


driver.find_element(by=By.XPATH,value='//label[text()="单行选择框"]/..//dd[text()="音乐"]').click()