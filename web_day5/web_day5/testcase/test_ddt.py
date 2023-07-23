"""
作者：张浩
时间：2023/7/20  15:11
邮箱：88302599@qq.com
"""
"""
ddt:Data Driver Test
ddt作用：把列表中的元素，分别传入案例中，每执行一条案例，会使用列表中的一个元素，不会重复，列表中的元素使用完后，案例停止执行
操作步骤
1、导包：from unittestreport import ddt,list_data
2、在测试类上面 @ddt
3、在需要引用测试数据的测试案例方法上面@list_data(),并发测试数据列表作为参数传入
4、在测试方法中新增一个参数，用来接收测试列表中的数据，供方法中引用
"""

import unittest
from unittestreport import ddt,list_data

testcase = [1,2,3,4,5]

@ddt
class Test_ddt(unittest.TestCase):

    @list_data(testcase)
    def test_ddt(self,item):
        print(item)