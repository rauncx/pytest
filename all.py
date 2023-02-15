import pytest

if __name__ == '__main__':
    pytest.main(['-vs'])
    # # 指定目录
    # pytest.main(['-vs', './testjk'])
    # # 指定用例
    # pytest.main(['-vs', './testjk/test_interface.py::test_04_func'])
    # # 失败用例重跑
    # pytest.main(['-vs', './test', '--reruns=1'])
    #  # -x表示只要要一个用例报错，那么测试停止
    # pytest.main(['-vs', './test', '-x'])
    # # --maxfail=2 出现两个用例失败就停止。
    # pytest.main(['-vs', './test', '--maxfail=2'])
    # # k: 根据测试用例的部分字符事指定测试用例。
    # pytest.main(['-vs', './test', '-k=two'])
    # # -n设置多线程
    # pytest.main(['-vs', './test', '-n=2'])
