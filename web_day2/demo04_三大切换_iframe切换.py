"""
作者：张浩
时间：2023/7/17  13:55
邮箱：88302599@qq.com
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
driver.get("https://qzone.qq.com/")
driver.implicitly_wait(15)
driver.maximize_window()


# frame = driver.find_element(by=By.XPATH,value='//iframe[@src="https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=https%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=https%3A//z.qzone.com/download.html&pt_no_auth=0"]')
# driver.switch_to.frame("login_frame")#通过iframe的id或者name属性切换
# driver.switch_to.frame(0)#通过iframe的索引切换
# driver.switch_to.frame(frame)#通过iframe的元素定位切换

loc_frame = (By.XPATH,'//iframe[@id="login_frame"]')

ec = EC.frame_to_be_available_and_switch_to_it(loc_frame)
WebDriverWait(driver,20,0.5).until(ec)



driver.find_element(by=By.LINK_TEXT,value="密码登录").click()