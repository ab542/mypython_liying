import json

from common.readyaml import ReadYamlData,get_testcase_yaml
from common.debugtalk import DebugTalk
from conf.operationConfig import OperationConfig
import allure

class BaseRequests:

    def __init__(self):
        self.read = ReadYamlData()
        self.conf=OperationConfig()

    def replace_load(self,data):
        """
        yaml文件替换解析有${}格式的数据
        :return:
        """
        str_data = data
        if not isinstance(data,str):
            str_data = json.dumps(data,ensure_ascii=False)
            print(str_data)
        for i in range(str_data.count('${')):
            if "${" in str_data and "}" in str_data:
                #index检测字符串是否子字符串，并找到字符串的索引位置
                start_index = str_data.index('$')
                end_index = str_data.index('}',start_index)
                print(start_index,end_index)
                ref_all_params = str_data[start_index:end_index+1]
                print(ref_all_params)
                #取出函数名
                func_name = ref_all_params[2:ref_all_params.index('(')]
                print(func_name)
                #取出参数名
                func_params = ref_all_params[ref_all_params.index('(')+1:ref_all_params.index(')')]
                print(func_params)
                #传输替换的参数获取对应的值--反射  getattr获取对象的属性/方法
                extracr_data = getattr(DebugTalk(),func_name)(*func_params.split(',') if func_params else "")
               # print(extracr_data)
                str_data=str_data.replace(ref_all_params,extracr_data)
               # print(str_data)
        #还原数据
        if data and isinstance(data,dict):
            data=json.loads(str_data)
        else:
            data=str_data
        return  data

    def specification_yaml(self,case_info):
        """
        规范yaml接口测试数据的写法
        :param case_info: list类型，调取case_infp[0]
        :return:
        """
        base_url = self.conf.get_envi('host')
        url = base_url + case_info['baseInfo']['url']
        api_name = case_info['baseInfo']['url']
        method = case_info['baseInfo']['method']
        header = case_info['baseInfo']['header']

        print(url)




#python反射是一种机制，它允许程序在运行时检查、访问和修改其自身的结构，例如类、对象、方法、属性等。
#setattr  getattr hasattr  deleattr dir-返回一个对象的所有属性和方法的名称列表
#type isinstance=检查对象的类型
#vars


if __name__ == '__main__':
    data = get_testcase_yaml('../testcase/Login/login.yaml')[0]
    # print(data)
    # base = BaseRequests()
    # data=base.replace_load(data)
    # print(data)
    req = BaseRequests()
    print(req.specification_yaml(data))


