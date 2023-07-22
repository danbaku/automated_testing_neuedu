"""
作者：张浩
时间：2023/7/19  14:05
邮箱：88302599@qq.com
"""

act_res = "登录成功"
expect_res = "登录失败"

try:
    assert act_res==expect_res
except Exception as e:
    print(e)
    raise e
else:
    print("案例成功")
