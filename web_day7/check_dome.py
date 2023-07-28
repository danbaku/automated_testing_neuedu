"""
作者：张浩
时间：2023/7/26  11:02
邮箱：88302599@qq.com
"""
import pytest

@pytest.mark.interface_case
def  test_check(login):
    assert 1==1


class zhanghao:

    @pytest.mark.level1
    @pytest.mark.web_case
    def check_zhanghao1(self,login_class,login):
        print("------check_zhanghao1-------")
        assert 100==100

    def check_zhanghao2(self,login):
        print("------check_zhanghao2-------")
        assert 100==100