import allure
import jsonpath
import pytest

from Day18.interface_pytest.conf.set_cof import read_yaml, write_ini_conf, read_ini_conf


@allure.epic('用户管理模块')
@allure.feature('用户登录')
@allure.story('用户登录接口')
@allure.tag('核心用例')
@allure.severity('CRITICAL')
@allure.title('用户登录 - 正常流程')
@allure.description('验证用户名密码正确时，登录接口返回成功信息')
@allure.label('owner', 'Jason')
@allure.link('http://154.12.20.250:5000/apidocs/', '接口文档')
@pytest.mark.parametrize('set_api_env', ['uat_env'], indirect=True)
@pytest.mark.parametrize('data', read_yaml('../test_data/login.yaml'))
def test_01_login(api, data, set_api_env):
    # 1. 先隐藏全量 data 和 set_api_env 参数（核心：excluded=True）
    allure.dynamic.parameter("data", "", excluded=True)  # 无标黄，生效
    allure.dynamic.parameter("set_api_env", "", excluded=True)
    # 2. 只添加当前用例需要的参数
    allure.dynamic.parameter("method", data["login"]["method"])
    allure.dynamic.parameter("path", data["login"]["path"])
    allure.dynamic.parameter("username", data["login"]["json"]["username"])
    with allure.step('1.发送请求'):
        res = api.request(**data['login'])
    with allure.step('2.获取响应结果'):
        print(res.json())
    with allure.step('3.获取token'):
        api.token = api.get_json_value(res.json(), 'token')
    with allure.step('4.将token写入到common_parm.ini文件中'):
        write_ini_conf('common_parm.ini', 'data', 'token', api.token)


@pytest.mark.parametrize('data', read_yaml('../test_data/login.yaml'))
def test_02_get_user_info(api, data):
    data['user_info']['headers']['Authorization'] = read_ini_conf('common_parm.ini', 'data', 'token')
    res = api.request(**data['user_info'])
    # print(res.json())
    user_id = api.get_json_value(res.json(), 'user_id')
    write_ini_conf('common_parm.ini', 'data', 'user_id', str(user_id))
    product_id = jsonpath.jsonpath(res.json(), '$..product_id')[0]
    write_ini_conf('common_parm.ini', 'data', 'id', str(product_id))


@pytest.mark.parametrize('data', read_yaml('../test_data/login.yaml'))
def test_03_add_balance(api, data):
    data['add_balance']['json']['user_id'] = read_ini_conf('common_parm.ini', 'data', 'user_id')
    res = api.request(**data['add_balance'])
    # print(res.json())


@pytest.mark.parametrize('data', read_yaml('../test_data/login.yaml'))
def test_04_get_goods_info(api, data):
    id_num = read_ini_conf('common_parm.ini', 'data', 'id')
    res = api.request(method=data['goods_info']['method'],
                      path=f"{data['goods_info']['path']}?id={id_num}",
                      expect=data['goods_info'].get('expect')
                      )


if __name__ == '__main__':
    pytest.main(['-sv', 'test_demo.py'])