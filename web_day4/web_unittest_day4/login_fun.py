"""
作者：张浩
时间：2022/8/25  9:09
邮箱：88302599@qq.com
"""
def login_func(name=None,pwd=None):
    if name !=None and pwd !=None:
        if name == 'zhanghao'  and  pwd == '123456':
            return {'code':0,'msg':'登录成功'}
        else:
            return {'code': 1, 'msg': '用户名或密码错误，登录失败'}
    else:
        return {'code': 2, 'msg': '用户名或密码不能为空'}