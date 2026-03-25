import json
import unittest

import jsonpath
from ddt import file_data, ddt

from Day17.interface_unittest.api_keys.api_keys import ApiKeys
from Day17.interface_unittest.conf.set_cof import write_ini_conf, read_ini_conf


@ddt
class TestApiKeys(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.api = ApiKeys('uat_env')
        cls.token = None

    @classmethod
    def tearDownClass(cls):
        write_ini_conf('common_parm.ini', data={'token': '', 'user_id': ''})

    @file_data('../test_data/login.yaml')
    def test_01_login(self, **kwargs):
        res = self.api.request(**kwargs['login'])
        print(res.json())
        TestApiKeys.token = self.api.get_json_value(res.json(), 'token')
        # print(self.token)
        # 将token写入到common_parm.ini文件中，方便后续接口关联
        write_ini_conf('common_parm.ini', 'data', 'token', self.token)

    @file_data('../test_data/login.yaml')
    def test_02_get_user_info(self, **kwargs):
        kwargs['user_info']['headers']['Authorization'] = self.token
        res = self.api.request(**kwargs['user_info'])
        print(res.json())
        user_id = self.api.get_json_value(res.json(), 'user_id')
        print(user_id)
        write_ini_conf('common_parm.ini', 'data', 'user_id',
                       str(user_id))
        print(jsonpath.jsonpath(res.json(), '$..product_id')[0])
        write_ini_conf('common_parm.ini', 'data', 'id',
                       str(jsonpath.jsonpath(res.json(), '$..product_id')[0]))

    @file_data('../test_data/login.yaml')
    def test_03_add_balance(self, **kwargs):
        kwargs['add_balance']['json']['user_id'] = read_ini_conf('common_parm.ini', 'data', 'user_id')
        res = self.api.request(**kwargs['add_balance'])
        # print(res.json())

    @file_data('../test_data/login.yaml')
    def test_04_get_goods_info(self, **kwargs):
        id_num = read_ini_conf('common_parm.ini', 'data', 'id')
        goods_info = kwargs['goods_info']
        res = self.api.request(method=goods_info['method'],
                               path=f"{goods_info['path']}?id={id_num}",
                               expect=goods_info.get('expect')
                               )


if __name__ == '__main__':
    unittest.main()