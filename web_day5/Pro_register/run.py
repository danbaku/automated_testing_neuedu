"""
作者：张浩
时间：2023/7/20  13:52
邮箱：88302599@qq.com
"""

import unittest
from unittestreport import TestRunner

suite = unittest.defaultTestLoader.discover(r'E:\class_2017\Pro_register\test_case')

runner = TestRunner(suite)

runner.run()