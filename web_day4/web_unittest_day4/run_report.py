"""
作者：张浩
时间：2023/7/19  15:35
邮箱：88302599@qq.com
"""
"""
pip install unittestreport
"""

import unittest
from unittestreport import TestRunner


suite= unittest.defaultTestLoader.discover(r"E:\class_2017\web_unittest_day4\testcase")

runner = TestRunner(suite,
                    title="XXX系统XX模块测试报告",
                    tester="张浩",
                    desc="测试覆盖率100%",
                    templates=2)

runner.run()