import time

import pytest
from common.readyaml import get_testcase_yaml
from common.sendrequests import SendRequests
from common.recordlog import logs

@pytest.fixture(scope="function",autouse=True,params=['11','22'],ids=['11','22'],name="test2")
def fixture_test(request):
    """前后置处理"""
    # print('----接口测试开始----')
    # yield
    # print('----接口测试结束----')
    return request.param

class TestLogin:

    # def setup_class(self):
    #     """在所有测试用例执行前只执行一次"""
    #     print("类的初始化工作，比如说创建对象，创建数据的连接")

    # def setup(self):
    #     """前置处理"""
    #     print("在每个测试用例方法运行前都要执行我的代码块")

    @pytest.mark.parametrize('params',get_testcase_yaml('D:/PycharmProjects/pythonProject01/testcase/Login/login.yaml'))
    def test_case01(self,params):
        from base.apiutil import BaseRequests
        base = BaseRequests()
        params = base.replace_load(params)
        url = params['baseInfo']['url']
        new_url = 'http://127.0.0.1:8787'+str(url)

      #  logs.info("获取到接口的地址：{}".format(new_url))
        logs.info("获取到接口的地址：{}".format(new_url))
        method = params['baseInfo']['method']
        headers = params['baseInfo']['header']
        data = params['testCase'][0]['data']
        print(data)
        send = SendRequests()
        res = send.run_main(url=new_url,data=data,header=None,method=method)
        print('接口实际返回值',res)

        assert res['msg'] == '登录成功'

        print('pytest测试框架-第一')
        print('获取到的参数为：',params)

    def test_case02(self,test2):
        print('pytest运行方式-第二')
        assert 1 > 2
        print('获取前置操作的参数：',test2)



    # def teardown(self):
    #     """后置处理"""
    #     print("在每个测试用例方法运行后都要执行我的代码块")
    #
    # def teardown_class(self):
    #     """在所有测试用例执行后只执行一次"""
    #     print("关闭数据库的连接")

if __name__ == '__main__':
    pytest.main()