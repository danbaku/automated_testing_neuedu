"""
作者：张浩
时间：2023/7/26  15:04
邮箱：88302599@qq.com
"""
import pytest


@pytest.fixture(scope="function")
def  login():
    print("----------------前置步骤---------------------")
    yield
    print("----------------后置步骤---------------------")



@pytest.fixture(scope="class")
def  login_class():
    print("----------------类级别前置步骤---------------------")
    yield
    print("----------------类级别后置步骤---------------------")