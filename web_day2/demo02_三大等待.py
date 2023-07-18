"""
作者：张浩
时间：2023/7/17  11:03
邮箱：88302599@qq.com
"""
"""
1、隐式等待：通过driver.implicitly_wait(最大等待时间)方式设置隐式等待时间，设置一次对driver的整个生命周期都有效果，如果元素超出最大等待时间，测报错
2、强制等待：time.sleep(n),代码运行到这，强制暂停几秒在往后执行
3、显示等待：
    1）导包
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
    2）创建一个等待条件对象
        语法：EC.条件(参数)
        EC的条件
            presence_of_element_located() 元素存在， 参数：元素定位的元组
            visibility_of_element_located() 元素可见， 参数：元素定位的元组
            element_to_be_clickable()  元素可点击， 参数：元素定位的元组
            new_window_is_opened()   新窗口打开    参数：当前页面的所有句柄
            frame_to_be_available_and_switch_to_it()   iframe可见并切换，参数：iframe的编号
    3）使用WebDriverWait创建一个等待对象
            参数1：driver对象
            参数2：等待最大时长（秒）
            参数3：轮询时间（每隔多长时间去查询一次元素）
    4）使用等待对象调用until方法，把等待条件作为参数传入
        
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.maximize_window()
# driver.implicitly_wait(15)#隐式等待

# driver.find_element(by = By.XPATH,value='//a[@href="https://haokan.baidu.com/?sfrom=baidu-top"]').click()

loc_vidoe = (By.XPATH,'//a[@href="https://haokan.baidu.com/?sfrom=baidu-top"]')

ec = EC.presence_of_element_located(loc_vidoe)#第一步，条件对象

WebDriverWait(driver,20,0.5).until(ec)#第二步，条件对象

driver.find_element(by = By.XPATH,value='//a[@href="https://haokan.baidu.com/?sfrom=baidu-top"]').click()
EC.frame_to_be_available_and_switch_to_it()






#
# driver.find_element(by=By.LINK_TEXT, value="登录").click()
#
# driver.find_element(by=By.ID, value="TANGRAM__PSP_11__userName").send_keys("17768148441")
#
# driver.find_element(by=By.ID, value="TANGRAM__PSP_11__password").send_keys("17768148441")
#
# driver.find_element(by=By.ID, value="TANGRAM__PSP_11__submit").click()