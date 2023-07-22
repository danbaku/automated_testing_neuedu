import unittest

from web_unittest_day4.register import register

class TestRegister(unittest.TestCase):

    def test_empty_params(self):

        result = register('', '', '')

        self.assertEqual(result, {"code": 0, "msg": "所有参数不能为空"})

    def test_existing_account(self):

        result = register('python', '123456', '123456')

        self.assertEqual(result, {"code": 0, "msg": "该账户已存在"})

    def test_password_mismatch(self):

        result = register('newuser', 'password1', 'password2')

        self.assertEqual(result, {"code": 0, "msg": "两次密码不一致"})

    def test_registration_success(self):

        result = register('newuser', 'password', 'password')

        self.assertEqual(result, {"code": 1, "msg": "注册成功"})

    def test_invalid_account_password_length(self):

        result = register('user', 'pass', 'pass')

        self.assertEqual(result, {"code": 0, "msg": "账号和密码都必须大于18位"})