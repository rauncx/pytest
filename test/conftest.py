import pytest

@pytest.fixture(scope='function',autouse=False,params=['测试', '参数', '快下班了'])
def my_fixture(request):    # request，获取params配置的参数
    # print('这是前置的方法，可以实现部分以及全部用例的前置')
    # yield   # 加上yield可以设置后置
    # print('这是后置的方法，可以实现部分以及全部用例的后置')

    print('这是前置的方法，可以实现部分以及全部用例的前置')
    yield request.param   # 有前后置操作时可以通过yield传参数
    print('这是后置的方法，可以实现部分以及全部用例的后置')

    # return request.param  # 传参数，不然其他方法调用时获取不到参数