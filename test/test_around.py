
'''
测试前后置
'''

import pytest

@pytest.fixture(scope='function',autouse=False,params=['测试', '参数', '快下班了'], ids=['qq','cs','s'], name='ruan')
def my_fixture(request):    # request，获取params配置的参数
    # print('这是前置的方法，可以实现部分以及全部用例的前置')
    # yield   # 加上yield可以设置后置
    # print('这是后置的方法，可以实现部分以及全部用例的后置')

    # print('这是前置的方法，可以实现部分以及全部用例的前置')
    # yield request.param   # 有前后置操作时可以通过yield传参数
    # print('这是后置的方法，可以实现部分以及全部用例的后置')

    return request.param  # 传参数，不然其他方法调用时获取不到参数


class TestAround:

    '''
    # 这个方法在所以用例之前只执行一次
    def setup_class(self):
        print('在每个类执行前的初始化的工作，比如：创建日志对象、创建数据库的连接、创建接口的请求')

    #  在每个用例之前都执行一次
    def setup_method(self):
        print('在执行测试用例之前初始化的代码：打开浏览器，加载网页\n')
    '''

    def test_front(self,my_fixture):
        print('测试一些前后置。。。\n')
        print('----'+str(my_fixture))   # 获取了参数，装饰器那里设置了多少参数就执行多少次

    def test_behind(self):
        print('测试一下前后置，测试一些前后置........\n')


    '''
    def teardown_method(self):
        print('在执行测试用例之后的扫尾代码：关闭浏览器\n')

    def teardown_class(self):
        print('在每个类执行后的扫尾工作，比如：销毁日志对象、销毁数据库的连接、销毁接口的请求')
    '''