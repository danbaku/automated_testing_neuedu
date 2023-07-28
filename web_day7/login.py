"""
作者：张浩
时间：2023/7/26  14:16
邮箱：88302599@qq.com
"""
import pytest

@pytest.fixture(autouse=True)
def  login():
    print("----------------前置步骤---------------------")
    yield
    print("----------------后置步骤---------------------")