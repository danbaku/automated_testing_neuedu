# """
# 作者：mrqc
# 时间：2023/7/16 10:57
# """
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
#
# # driver的基本操作方法
# # 打开指定页面
# driver.get("http://www.baidu.com")
#
# # # 页面最大化
# # driver.maximize_window()
# #
# # # 页面最小化
# # driver.minimize_window()
# #
# # # 页面刷新
# # driver.refresh()
# #
# # # 进入下一页
# # driver.forward()
# #
# # # 回到上一页
# # driver.back()
# #
# # # 当前页面截图
# # driver.save_screenshot("res.png")
# #
# # # 关闭浏览器
# # driver.close()
#
# # diver的对象属性
#
# driver.get("http://www.taobao.com")
#
# # 获取title
# # t = driver.title
# #
# # print(t)
# #
# # driver.close()
#
# # 获取页面源码
# # page_code=driver.page_source
# #
# # print(page_code)
# #
# # driver.close()
#
# # 当前所有页面的句柄
# # page_h = driver.window_handles
# #
# # print(page_h)
# #
# # driver.close()
#

# 浏览器控件定位
import time

from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 通过id属性定位元素
# elm_text=driver.find_element(by = By.ID, value="kw")
# elm_text.send_keys("自动化测试")

# 通过name属性定位元素
# driver.find_element(by=By.NAME, value="wd").send_keys("自动化测试")

# 通过class属性定位元素
# driver.find_element(by=By.CLASS_NAME, value="s_ipt").send_keys("自动化测试")

# 通过标签定位元素
# driver.find_element(by=By.TAG_NAME, value="input").send_keys("自动化测试")

# 只针对a标签
# driver.find_element(by=By.LINK_TEXT,value="新闻").click()

# 通过元素的Xpath表达式进行定位
# driver.find_element(by=By.XPATH , value='//input[@id = "kw"]').send_keys("自动化测试")

time.sleep(5)

driver.close()