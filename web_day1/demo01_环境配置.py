"""
作者：张浩
时间：2023/7/16  10:58
邮箱：88302599@qq.com
"""
"""
python

pycharm

selenium:
1、命令：pip install selenium==4.4.0
2、cmd命令行执行上面命令
    备注：如果报错【time out】，pip install selenium==4.4.0 --default-time=1000
3、pip list检查是否安装成功

chromedriver
1、下载地址：https://registry.npmmirror.com/binary.html?path=chromedriver/
2、下载与浏览器对应的版本，如果找不到对应版本，请下载版本号最接近的版本，但是chromedriver不能高于浏览器版本
3、下载后，把chromedriver.exe放到python安装目录下
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
