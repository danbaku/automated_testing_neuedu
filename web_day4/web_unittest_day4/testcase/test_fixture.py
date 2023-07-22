"""
作者：张浩
时间：2023/7/19  14:41
邮箱：88302599@qq.com
"""


import unittest

class Test_fix(unittest.TestCase):


    def test_001(self):
        print("----------test001------------")
    def test_002(self):
        print("----------test002------------")
    def test_003(self):
        print("----------test003------------")

    def setUp(self):
        print("案例级别前置步骤")
    def tearDown(self):
        print("案例级别后置步骤")
    @classmethod
    def setUpClass(cls):
        print("类级别前置步骤")

    @classmethod
    def tearDownClass(cls):
        print("类级别后置步骤")