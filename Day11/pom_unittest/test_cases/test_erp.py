'''
    erp的测试流程：测试用例层级，用于管理测试用例和编写测试代码
'''
import unittest

from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from Day11.pom_unittest.page_object.login_page import LoginPage
from Day11.pom_unittest.page_object.vendor_page import VendorPage


@ddt
class TestErp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.vp = VendorPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @file_data('../test_data/erp.yaml')
    def test_01_login(self, **kwargs):
        self.lp.login(kwargs['login']['user'], kwargs['login']['pwd'])

    @file_data('../test_data/erp.yaml')
    def test_02_vendor(self, **kwargs):
        self.vp.add_supplier(kwargs['vendor']['name'], kwargs['vendor']['tele'])


if __name__ == '__main__':
    unittest.main()
