"""
作者：张浩
时间：2023/7/16  14:19
邮箱：88302599@qq.com
"""

from selenium import webdriver
driver = webdriver.Chrome()

#---------------------driver的基本操作方法-----------------------------
# driver.get("http://www.baidu.com")#打开指定页面
#
# driver.maximize_window()#页面最大化
#
# driver.minimize_window()#页面最小化
#
# driver.refresh()#刷新页面
#
# driver.forward()#进入下一页
# driver.back()#回到上一页
#

# driver.save_screenshot("res.png")#当前页面截图

# driver.close()#关闭浏览器

#----------------------driver的对象属性-------------------------
driver.get("http://www.taobao.com")#打开指定页面

# t= driver.title#获取页面标题
# print(t)

# page_code=driver.page_source#获取页面源码


# page_h=driver.window_handles#当前所有页面的句柄
#
# print(page_h)
# driver.close()