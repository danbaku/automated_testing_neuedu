"""
作者：张浩
时间：2023/7/17  9:57
邮箱：88302599@qq.com
"""
"""
/:根节点
//:子孙结点


/或者//后面需要加上需要定位的标签名称，*代表所有标签


[]:谓语条件
1、索引取值[索引值]：Xpath的索引是从1开始
2、通过标签的属性定位标签[@属性名=属性值]
3、通过标签中文本定位


谓语中函数
1、contains(参数1,参数2):匹配符合 参数1中包含参数2的条件 的数据
        匹配标签里的文本：//a[contains(text(),"hao")]
        匹配标签里的属性：//a[contains(@href,"hao123")]

2、start-with(参数1,参数2):匹配符合 参数1中以参数2为开头的条件 的数据
        匹配标签里的文本：//a[start-with(text(),"hao")]
        匹配标签里的属性：//a[start-with(@href,"hao123")]
        
        
路径定位：根据节点父子关系定位元素


"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.maximize_window()
driver.implicitly_wait(15)

# driver.find_element(by=By.XPATH,value='//a[text()="新闻"]').click()#通过文本

#通过标签属性
# driver.find_element(by=By.XPATH,value='//a[@href="http://news.baidu.com"]').click()

#通过标签属性的包含关系
# driver.find_element(by=By.XPATH,value='//a[contains(@href,"hao123")]').click()

#通过的包含关系
driver.find_element(by=By.XPATH,value='//a[contains(text(),"hao")]').click()




# li_elm=driver.find_elements(by=By.XPATH,value='//a[contains(@class,"c-font-normal")]')
# print(li_elm)
#
# li_elm[1].click()




