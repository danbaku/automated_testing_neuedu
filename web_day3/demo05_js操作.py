"""
作者：张浩
时间：2023/7/18  11:18
邮箱：88302599@qq.com
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
driver.implicitly_wait(15)
driver.maximize_window()




# driver.find_element(by=By.ID,value="fromStationText").click()
# driver.find_element(by=By.ID,value="fromStationText").send_keys("北京西",Keys.ENTER)
#
# driver.find_element(by=By.ID,value="toStationText").click()
# driver.find_element(by=By.ID,value="toStationText").send_keys("南京南",Keys.ENTER)


elm_start=driver.find_element(by=By.ID,value="fromStationText")
print(elm_start)
# js="arguments[0].value=arguments[1]"
# driver.execute_script(js,elm_start,"北京西")


# elm_end=driver.find_element(by=By.ID,value="toStationText")
# js="arguments[0].value=arguments[1]"
# driver.execute_script(js,elm_end,"南京南")


# elm_date=driver.find_element(by=By.ID,value="train_date")
# js="arguments[0].value=arguments[1]"
# driver.execute_script(js,elm_date,"2023-07-20")
#
# driver.find_element(by=By.ID,value="isStudentDan").click()
#
# driver.find_element(by=By.ID,value="search_one").click()
