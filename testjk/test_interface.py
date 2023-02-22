import pytest

def test_04_func():
    print("函数")

class TestInterface:

    def test_03_jk(self):
        print('testjk')

    @pytest.mark.smoke
    def test_loginjk(self):
        print("测试登录接口")


