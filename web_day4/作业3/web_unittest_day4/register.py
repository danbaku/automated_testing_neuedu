users = [{'user':'python','password':'123456'}]

def register(username,pwd1,pwd2):
    if not all ([username,pwd1,pwd2]):
        return {"code":0,"msg":"所有参数不能为空"}
    for u in users:
        if username == u['user']:
            return {"code":0,"msg":"该账户已存在"}
    else:
        if pwd1 != pwd2:
            return {"code":0,"msg":"两次密码不一致"}
        else:
            if 6<=len(username)>=6 and 6<=len(pwd1)>=18:
                users.append({'user':username,'password':pwd2})
                return {"code":1,"msg":"注册成功"}
            else:
                return {"code": 0, "msg": "账号和密码都必须大于18位"}