"""
作者：张浩
时间：2023/7/26  10:53
邮箱：88302599@qq.com
"""
import unittest
from unittestreport import ddt,list_data
list1 = [1,2,4,5,6,7,8]

@ddt
class Test_Ut(unittest.TestCase):

    def test_001(self):
        assert 1 == 1

    @list_data(list1)
    def test_ddt(self,item):
        print(item)