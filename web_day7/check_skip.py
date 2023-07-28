"""
作者：张浩
时间：2023/7/26  14:03
邮箱：88302599@qq.com
"""
import  pytest
from web_day7.login import login

a=99

@pytest.mark.skipif(a==99,reason="aaa")
def test_001():
    assert 100==100

def test_002():
    assert 100==100
