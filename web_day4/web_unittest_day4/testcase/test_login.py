"""
作者：张浩
时间：2023/7/19  15:02
邮箱：88302599@qq.com
"""
import unittest
from web_unittest_day4.login_fun import login_func
class Test_Login(unittest.TestCase):


    def test_login_pass(self):
        #一、准备数据（请求数据、预期结果）
        data={"name":"zhanghao","pwd":"123456"}#请求数据
        expect_res = {'code':0,'msg':'登录成功'}#预期结果

        #二、用准备好的请求数据，请求被测函数
        act_res=login_func(name =data["name"],pwd = data["pwd"])

        #三、断言
        assert act_res==expect_res

    def test_login_usererror_fail(self):
        # 一、准备数据（请求数据、预期结果）
        data = {"name": "zhanghao11", "pwd": "123456"}  # 请求数据
        expect_res = {'code': 1, 'msg': '用户名或密码错误，登录失败'}  # 预期结果

        # 二、用准备好的请求数据，请求被测函数
        act_res = login_func(name=data["name"], pwd=data["pwd"])

        # 三、断言
        assert act_res == expect_res

    def test_login_pwderror_fail(self):
        # 一、准备数据（请求数据、预期结果）
        data = {"name": "zhanghao", "pwd": "1234562"}  # 请求数据
        expect_res = {'code': 1, 'msg': '用户名或密码错误，登录失败'}  # 预期结果

        # 二、用准备好的请求数据，请求被测函数
        act_res = login_func(name=data["name"], pwd=data["pwd"])

        # 三、断言
        assert act_res == expect_res