import json

import yaml
import os

from conf.setting import FILE_PATH

def get_testcase_yaml(file):
    """
    获取yaml文件的数据
    :param file: yaml文件的路径
    :return:获取到的yaml文件
    """
    try:
         with open(file,'r',encoding='utf-8') as f:
             yaml_data = yaml.safe_load(f)



             return yaml_data
    except Exception as e:
        print(e)



class ReadYamlData:

   """读取yaml数据，以及写入结果数据到yaml文件"""

   def __init__(self,yaml_file=None):
       if yaml_file is not None:
           self.yaml_file = yaml_file
       else:
           self.yaml_file = 'login.yml'

   def write_yaml_data(self,value):
       """
       写入数据到yaml文件
       :param value: （dict）写入的数据
       :return:
        os.system(file_path)  不存在 就创建
        allow_unicode=True) 允许写入中文 不会乱码
        mode='a'追加写入
        mode='w' 清空重新写入
       """
       file = None
       #file_path = r'../extract.yaml'
       file_path = FILE_PATH['extract']
       if not os.path.exists(file_path):
           os.system(file_path)

       #w 清空后写入 a在原有基础上写入
       try:
           file = open(file_path, mode='a', encoding='utf-8')
           if isinstance(value, dict):
               write_data = yaml.dump(value, allow_unicode=True, sort_keys=False)
               file.write(write_data)
           else:
               print('写入到【extract.yaml】的数据必须为字典数据类型')
       except Exception as e:
           print(e)
       finally:
           file.close()

   def get_extract_yaml(self,node_name):
       """
       读取接口提取的变量值
       :param node_name:yaml文件的key值
       :return:
       """
       file_path = FILE_PATH['extract']
       if os.path.exists(file_path):
           pass
       else:
           print('extract.yaml不存在')
           file = open(file_path, 'w')
           file.close()
           print('extract.yaml创建成功！')

       with open(file_path, 'r', encoding='utf-8') as rf:
           extract_data = yaml.safe_load(rf)
           return extract_data[node_name]


if __name__ == '__main__':
    res = get_testcase_yaml('../testcase/Login/login.yaml')[0]
    url = res['baseInfo']['url']
    new_url = 'http://127.0.0.1:8787'+url
    method=res['baseInfo']['method']
    data = res['testCase'][0]['data']
    from common.sendrequests import SendRequests

    send = SendRequests()
    res = send.run_main(method=method,url=new_url,data=data,header=None)
    print(res)

    token = res.get('token')
    print(token)

    write_data={}
    write_data['Token'] = token

    read = ReadYamlData()
    read.write_yaml_data(write_data)


    #python常用的数据类型：str list dict set-集合 tuple-元组
    # json序列化-对象-字典转换为json字符串格式和 反序列化
    json_str = json.dumps(res,ensure_ascii=False)
    print(json_str)

    json_dict = json.loads(json_str)
    print(json_dict)

    restoken = read.get_extract_yaml('Token')
    print(restoken)
