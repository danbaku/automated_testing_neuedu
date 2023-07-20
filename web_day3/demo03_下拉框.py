"""
作者：张浩
时间：2023/7/18  10:53
邮箱：88302599@qq.com
"""
"""
下拉框
第一种:针对原生的html的<select>标签
from selenium.webdriver.support.select import Select

第二种：前端框架组件实现的
只能一步一步点
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("E:/class_2017/web_day2/test.html")
driver.maximize_window()
driver.implicitly_wait(15)

elm_sel=driver.find_element(by=By.NAME,value="sheng")

s1=Select(elm_sel)
time.sleep(2)
# s1.select_by_value("js")
# s1.select_by_index(2)
s1.select_by_visible_text("广东")