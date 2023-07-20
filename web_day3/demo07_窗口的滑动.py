"""
作者：张浩
时间：2023/7/18  13:48
邮箱：88302599@qq.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# driver.get("https://layui.dev/docs/2.8/form/#login")
driver.get("https://www.12306.cn/index/")
driver.maximize_window()
driver.implicitly_wait(15)

btn=driver.find_element(by=By.LINK_TEXT ,value='常见问题')

# 第一种方式，滚动到元素可见位置,返回元素的坐标位置。备注，这个方法不能加括号
# res = btn.location_once_scrolled_into_view
# print(res)


#第二种方式：使用js滚动到指定元素位置
# js="arguments[0].scrollIntoView()"
# driver.execute_script(js,btn)

#第三种方式：使用js滚动指定的像素距离

js="window.scrollBy(0,arguments[0])"
driver.execute_script(js,500)
driver.execute_script(js,500)