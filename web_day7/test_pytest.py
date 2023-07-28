"""
作者：张浩
时间：2023/7/26  10:49
邮箱：88302599@qq.com
"""
import pytest
from web_day7.login import login


@pytest.mark.interface_case
def test_demo(login):
    print("---------- 这是一条案例---------------")
    assert 100==100



class Test_Py:
    @pytest.mark.web_case
    @pytest.mark.skip
    def test_001(self):
        assert 100 == 11
