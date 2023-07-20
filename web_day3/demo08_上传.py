"""
作者：张浩
时间：2023/7/18  14:47
邮箱：88302599@qq.com
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://layui.dev/docs/2.8/upload/#examples")
driver.implicitly_wait(15)
driver.maximize_window()

# 第一种方式：找到type=file的input标签，直接send_keys文件路径即可
# driver.find_element(by=By.XPATH,value='//button[@id="ID-upload-demo-btn"]/../input').send_keys(r"C:\Users\zhanghao\Pictures\22.jpg")


#-----------------------------------------------------------
"""
第二种方式：pywinauto(只能在windows下使用，必须关闭360)
1、安装：pip install  pywinauto
"""

from pywinauto.keyboard import send_keys

driver.find_element(by=By.ID,value="ID-upload-demo-btn-2").click()
time.sleep(3)
send_keys(r'"C:\Users\zhanghao\Pictures\22.jpg"')
send_keys(r'"C:\Users\zhanghao\Pictures\33.jpg"')
send_keys("{VK_RETURN}")