import unittest
from ddt import ddt, data, unpack, file_data

from Day8.Web_keys.web_keys import WebKeys


@ddt  # 声明ddt
class TestDDT(unittest.TestCase):
    # @data('huangcaicai', '小助理')
    @data(['huangcaicai', '小助理'], ['zhangsan', '李四'])  # 用于管理测试数据
    @unpack  # 二次解包数据
    def test_01_login(self, name, pwd):
        # def test_01_login(self, name):
        print('这是login测试用例')
        print(name)
        print(pwd)

    @file_data('./search.yaml')  # 专用于解析yaml文件内容
    def test_01_search(self, common, txt):
        driver = WebKeys('Chrome')
        driver.open_url(common['url'])
        driver.input(**common['input'], text=txt)
        driver.click(**common['click'])
        driver.wait(common['wait'])
        # print(common)
        # print(common['input']['value'])
        # print(common['click']['value'])


if __name__ == '__main__':
    unittest.main()
