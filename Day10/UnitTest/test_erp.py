import unittest
from selenium.webdriver.support.wait import WebDriverWait
from Day8.Web_keys.web_keys import WebKeys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time


class TestErp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebKeys('Chrome')
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_login(self):
        self.driver.open_url('http://39.101.122.147:3000/user/login')
        self.driver.input('id', 'loginName', 'jsh')
        self.driver.input('id', 'password', '123456')
        self.driver.input('id', 'inputCode', self.driver.get_code('xpath', '//img[@data-v-4f5798c5]'))
        self.driver.click('xpath', '//button[@data-v-4f5798c5]')
        # self.driver.assert_text('xpath', '//span[contains(text(), "退出登录")]/parent::a', '退出登录')
        self.driver.wait(5)



if __name__ == '__main__':
    unittest.main()


