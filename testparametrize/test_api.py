import os
import pytest
import requests
from testparametrize.yaml_util import YamlUtil

class TestApi():
    # 这样获取不到yaml文件的路径
    # @pytest.mark.parametrize('args', YamlUtil('test_api.yaml').read_yaml())
    @pytest.mark.parametrize('args', YamlUtil(os.getcwd()+'/testparametrize/test_api.yaml').read_yaml())
    def test_login(self, args):
        # print(args)
        # 路径，获取yaml配置文件中设置的url
        url = args['request']['url']
        # 需要传入的数据,获取yaml配置文件中设置的参数
        params = args['request']['params']
        # 发送get请求
        res = requests.get(url, params=params)
        print(res.text)