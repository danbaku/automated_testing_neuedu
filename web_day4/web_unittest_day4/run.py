"""
作者：张浩
时间：2023/7/19  15:27
邮箱：88302599@qq.com
"""

import unittest

#1、创建一个测试套件，把测试案例加载进去
#1）创建测试套件的对象
suite = unittest.TestSuite()
#2) 创建一个案例加载器
load = unittest.TestLoader()
#3)把测试案例加载到测试套件中
suite.addTest(load.discover(r"E:\class_2017\web_unittest_day4\testcase"))

#2、创建案例运行器
runner =  unittest.TextTestRunner()

#3、运行案例
runner.run(suite)
