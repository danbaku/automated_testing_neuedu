"""
作者：张浩
时间：2023/7/16  15:22
邮箱：88302599@qq.com
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#1、通过元素ID属性定位元素(重点)
# elm_text=driver.find_element(by =By.ID,value="kw")
# elm_text.send_keys("自动化测试")

#2、通过元素name属性定位元素(重点)
# driver.find_element(by=By.NAME,value="wd").send_keys("页面定位方式")

#3、通过元素的class属性定位元素（一般不用，因为元素不唯一）
# driver.find_element(by=By.CLASS_NAME,value="s_ipt").send_keys("class定位")

#4、通过元素的标签名称定位元素（一般不用，因为元素不唯一）
# driver.find_element(by=By.TAG_NAME,value="input").send_keys("标签名称定位")

#5、通过超链接的文本定位，仅限于a标签
# driver.find_element(by=By.LINK_TEXT,value="新闻").click()

#6、通过元素的Xpath表达式定位(重点)
driver.find_element(by=By.XPATH,value='//input[@id="kw"]').send_keys("Xpath定位")

time.sleep(5)

driver.close()