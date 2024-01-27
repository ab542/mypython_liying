import random

from common.readyaml import ReadYamlData

class DebugTalk:

    def __init__(self):
        self.read=ReadYamlData()
        pass

    def get_extract_order_data(self,data,randoms=None):
        if randoms not in [0,-1,-2]:
            return data[randoms-1]

    def get_extract_data(self,node_name,randoms=None):
        """
        获取extract.yaml的数据
        :param node_name: key值
        :param random: 随机读取extract.yaml中的数据
        :return:
        """
        data = self.read.get_extract_yaml(node_name)
        print(data)
        if randoms is not None:
            irandom = int(randoms)
            data_value = {
              irandom: self.get_extract_order_data(data,irandom),
              0 : random.choice(data),
              -1: ','.join(data),
              -2: ','.join(data).split(',')
            }
            data=data_value[irandom]
        return data

    def md5_params(self,params):
        return params

if __name__ == '__main__':
    debugtalk = DebugTalk()
    data = debugtalk.get_extract_data("product_id",-2)
    print(data)
