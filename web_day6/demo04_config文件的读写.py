"""
作者：张浩
时间：2023/7/25  15:08
邮箱：88302599@qq.com
"""
#------------------.cfg或,ini后缀配置文件解析----------------------------
# from  configparser import ConfigParser
#
# #1、创建配置文件的解析对象
# cp  = ConfigParser()
#
# #2、加载配置文件
# cp.read("E:\class_2017\web_day6\config\config.ini",encoding="utf-8")
#
#
# #3、读取具体的配置项
# res = cp.get("database","db")
#
# print(res)

#---------------------------yaml文件的解析------------------------------------

import  yaml

with open("E:\class_2017\web_day6\config\config.yaml","r",encoding="utf-8") as f:
    res = yaml.load(f,Loader=yaml.Loader)

print(res)