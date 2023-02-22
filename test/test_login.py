import pytest


class TestLogin:

    @pytest.mark.smoke
    def test_login(self):
        print("测试登录")

    login = "false"
    @pytest.mark.skipif(login =="false", reason="未登录成功就跳过这个测试用例")
    def test_01_vaili(self):
        print("pytest")

    @pytest.mark.skip("跳过这个测试用例")  # 跳过这个测试用例
    def test_py(self):
        print("跳过这个测试用例")

    @pytest.mark.user
    def test_user(self):
        print("测试用户管理")