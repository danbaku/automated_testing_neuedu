import unittest

from unittestreport import TestRunner

suite= unittest.defaultTestLoader.discover(r"E:\个人\实训\三年级第二次实训\web_day4\web_unittest_day4\testcase")

runner = TestRunner(suite,
                    title="XXX系统XX模块测试报告",
                    tester="",
                    desc="测试覆盖率100%",
                    templates=2)

runner.run()