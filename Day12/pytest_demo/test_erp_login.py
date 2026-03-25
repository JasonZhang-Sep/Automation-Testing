import pytest
from Day8.Web_keys.web_keys import WebKeys


@pytest.fixture()
def wk():
    """创建浏览器对象"""
    driver = WebKeys('Chrome')
    yield driver
    driver.quit()


class TestERP():
    @pytest.mark.login
    @pytest.mark.parametrize('username, password', [('jsh', '123456'), ('admin', '123456')])
    def test_01_login(self, wk, username, password):
        wk.open_url('http://39.101.122.147:3000/user/login')
        wk.input('id', 'loginName', username)
        wk.input('id', 'password', password)
        wk.input('id', 'inputCode', wk.get_code('xpath', '//img[@data-v-4f5798c5]'))
        wk.click('xpath', '//button[@data-v-4f5798c5]')
        wk.wait(5)

    @pytest.mark.vendor
    def test_02_vendor(self, wk):
        print('这是供应商测试用例')


if __name__ == '__main__':
    pytest.main(['-sv', 'test_erp_login.py' ])