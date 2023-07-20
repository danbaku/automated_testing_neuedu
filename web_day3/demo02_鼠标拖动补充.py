"""
作者：张浩
时间：2023/7/18  10:44
邮箱：88302599@qq.com
"""

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
driver.maximize_window()
driver.implicitly_wait(15)

driver.switch_to.frame("iframeResult")

btn_small = driver.find_element(by=By.ID,value="draggable")

btn_big = driver.find_element(by=By.ID,value="droppable")


ac=ActionChains(driver)

ac.click_and_hold(btn_small)

ac.move_to_element(btn_big)

ac.release()

ac.perform()