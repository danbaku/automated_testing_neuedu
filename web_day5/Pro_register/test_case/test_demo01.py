"""
作者：张浩
时间：2023/7/20  13:35
邮箱：88302599@qq.com
"""
import unittest
from register_fun import register


class Test_reg(unittest.TestCase):


    def test_reg_success(self):
        #1、准备数据
        data = {"user":"zhanghao","passwd1":"12345678","passwd2":"12345678"}
        expect_res = {"code":1,"msg":"注册成功"}

        #2、请求被测函数，获得实际结果
        act_res = register(username=data["user"],pwd1 = data["passwd1"],pwd2=data["passwd2"])

        print("预期结果",expect_res)
        print("实际结果", act_res)

        #3、断言
        assert expect_res==act_res

    def test_reg_fail_user_null(self):
        #1、准备数据
        data = {"user":"","passwd1":"12345678","passwd2":"12345678"}
        expect_res = {"code":0,"msg":"所有参数不能为空"}

        #2、请求被测函数，获得实际结果
        act_res = register(username=data["user"],pwd1 = data["passwd1"],pwd2=data["passwd2"])

        print("预期结果",expect_res)
        print("实际结果", act_res)

        #3、断言
        assert expect_res==act_res


    def test_reg_fail_pwd1_null(self):
        #1、准备数据
        data = {"user":"zhanghao","passwd1":"","passwd2":"12345678"}
        expect_res = {"code":0,"msg":"所有参数不能为空"}

        #2、请求被测函数，获得实际结果
        act_res = register(username=data["user"],pwd1 = data["passwd1"],pwd2=data["passwd2"])

        print("预期结果",expect_res)
        print("实际结果", act_res)

        #3、断言
        assert expect_res==act_res


    def test_reg_fail_pwd2_null(self):
        #1、准备数据
        data = {"user":"zhanghao","passwd1":"12345678","passwd2":""}
        expect_res = {"code":0,"msg":"所有参数不能为空"}

        #2、请求被测函数，获得实际结果
        act_res = register(username=data["user"],pwd1 = data["passwd1"],pwd2=data["passwd2"])

        print("预期结果",expect_res)
        print("实际结果", act_res)

        #3、断言
        assert expect_res==act_res