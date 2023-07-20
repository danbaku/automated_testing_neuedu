"""
作者：张浩
时间：2023/7/18  10:28
邮箱：88302599@qq.com
"""

"""
鼠标操作
1、导包：from selenium.webdriver import ActionChains
2、鼠标操作
    1）创建一个鼠标对象：ac=ActionChains(driver)
    2）鼠标左键点住不放：ac.click_and_hold(需要拖动的控件)
    3）拖动鼠标到指定坐标：ac.move_by_offset(xoffset=120,yoffset=0)
    4）释放鼠标：ac.release()
3、提交鼠标操作：ac.perform()

#常见的鼠标操作
#ac.click(元素定位) 鼠标左键单击
#ac.context_click()鼠标右键单击
#ac.double_click() 鼠标左键双击

"""
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://layui.dev/docs/2.8/slider/#examples")
driver.maximize_window()
driver.implicitly_wait(15)
btn = driver.find_element(by=By.XPATH,value='//div[@id="ID-slider-demo"]//div[@class="layui-slider-wrap-btn"]')


#---------------------鼠标操作------------------------
#1、创建一个鼠标对象
ac=ActionChains(driver)

#2、鼠标左键点住不放
ac.click_and_hold(btn)

#3、拖动鼠标
ac.move_by_offset(xoffset=120,yoffset=0)

#4、释放鼠标
ac.release()

#5、提交鼠标执行
ac.perform()


#常见的鼠标操作
#ac.click(元素定位) 鼠标左键单击

#ac.context_click()鼠标右键单击

#ac.double_click() 鼠标左键双击