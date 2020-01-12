# -*- coding: UTF-8 -*-
# 导入库
import requests,json


class http:
    def __init__(self):
        # session管理
        self.session = requests.session()
    #     基础的host地址
        self.url=''
        self.result=None
        self.jsonres=None
        self.relations={}

    def seturl(self,url):
        # 设置基础的url地址
        self.url=url
    def post(self,path,params):
        """
        设置请求的地址和参数
        :param path: 请求的地址
        :param params: 请求的参数
        :return:
        """
        params=self.__get_relations(params)
        self.result=self.session.post(self.url+path,data=self.__get_data(params))
        self.jsonres=json.loads(self.result.text)
        print(self.jsonres)
    def addhearder(self,key,value):
        """
        在session里面添加的头部信息
        :param key:头的键
        :param value:头的值
        :return:
        """
        value=self.__get_relations(value)
        self.session.headers[key] = value
    def __get_data(self,params):
        """
        将标准的url格式参数转换为字典
        :param params: 输入的url参数字符串
        :return: 转换后的字典
        """
        if params is None or params=='':
            # 如果是空或者空字符串都返回NONE
            return None
        else:
            params_dict={}
            # 分割url字符串的键值对
            list_params=params.split('&')
            # 遍历键值对
            for items in list_params:
                # 如果键值对里面有等号,那么我们取=左边为键,右边为值
                # 主要是支持值里面传等号
                if items.find('=')>=0:
                    params_dict[items[0:items.find('=')]]=items[items.find('=')+1:]
                else:
                    # 如果没有等号直接处理键，值为空
                    params_dict[items]=None
            return params_dict
    def savajson(self,key,param_name):
        """
     保存关联的参数
        :param key: 需要保存的json里面的键
        :param param_name:保存后参数的名字
        :return
        """
        self.relations[param_name]=self.jsonres[key]
    def __get_relations(self,params):
        """
        将参数里面用到关联的地方，替换为关联后的值
        :param params: 关联前的参数
        :return: 关联后的结果
        """
        if params is None or params == '':
            return ''
        else:
            # 遍历当前保存后的参数字典
            # 然后把参数里面凡是符合：{keys}这种
            #形式的字符串，都替换为relations这个字典里面keys这个键的值
            for keys in self.relations:
                params=params.replace('{'+keys+'}',self.relations[keys])
        return params
