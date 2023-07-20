"""
作者：张浩
时间：2023/7/18  13:34
邮箱：88302599@qq.com
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://www.12306.cn/index/")
# driver.implicitly_wait(15)
# driver.maximize_window()
#
# url = "http://www.taobao.com"
# js= "window.open(arguments[0])"
# driver.execute_script(js,url)

def open_and_switch_newwin(driver,url):
    old_handler = driver.window_handles
    js = "window.open(arguments[0])"
    driver.execute_script(js,url)
    ec = EC.new_window_is_opened(old_handler)
    WebDriverWait(driver,20,0.5).until(ec)
    new_handler = driver.window_handles
    driver.switch_to.window(new_handler[-1])


driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")

open_and_switch_newwin(driver,"http://www.jd.com")