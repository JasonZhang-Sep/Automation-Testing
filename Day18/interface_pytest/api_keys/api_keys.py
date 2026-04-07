import json

import jsonpath
from requests import request

from Day17.interface_unittest.conf.set_cof import read_ini_conf, write_ini_conf
import requests


class ApiKeys:
    def __init__(self):
        self.env = None # env的默认属性

    def set_env(self, env):
        self.env = env

    # 基于request统一封装的模拟请求。
    def request(self, method, path=None, headers=None, expect=None, **kwargs):
        '''
            :param method: 请求方法的定义
            :param url: 在不同环境下，url的IP和端口是会有改变，但是接口路径是不会发生变化的。
                基于此特性，我们可以拆解url，进行相关的配置读取操作。从而满足不同环境下的接口测试
            :param headers: 需要新增的请求头参数，基于set_headers方法实现对请求时，请求头信息
                的补全操作
            :param expect: 期望结果，用于断言（可选）
            :param kwargs: 其他请求参数的定义
            :return: 返回response 对象。
        '''
        # url等于ini文件里面的host拼接path组成的
        url = self.set_url(path)
        headers = self.set_headers(headers)
        res = request(method=method, url=url, headers=headers, **kwargs)
        if expect:
            self.assert_text(expect, res)
        return res


    # url拼接
    def set_url(self, path):
        url = read_ini_conf('server.ini', self.env, 'host')
        if path:
            url = url + path
        return url

    # 请求头设置
    def set_headers(self, headers):
        # 定义默认请求头
        base_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/145.0.0.0 Safari/537.36'
        }
        if headers:
            base_headers.update(headers)
        # 如果运行过程中产生了token，将写入到common_parm.ini文件中。后续每次操作去读common_parm文件,将token值写入到headers中。
        if read_ini_conf('common_parm.ini', 'data', 'token'):
            token = read_ini_conf('common_parm.ini', 'data', 'token')
            base_headers['Authorization'] = token
        return base_headers

    # jsonpath的封装，获取指定的数据
    def get_json_value(self,res, key):
        values = jsonpath.jsonpath(res, f'$..{key}')
        if not values:  # 等价于 if values == False:
            return values

        return values[0] if len(values) == 1 else values

    # 断言
    def assert_text(self, expect, res):
        '''
        根据 expect字典进行断言
        expect格式：{'message': 'Login successful', 'code': 200}
        '''
        for key, expected_value in expect.items():
            reality = self.get_json_value(res.json(), key)
            print(f'期望结果：{expected_value}，实际结果：{reality}')
            assert expected_value == reality, f'''
            期望结果：{expected_value}，
            实际结果：{reality}',
            断言结果：{expected_value} != {reality}
                 '''








