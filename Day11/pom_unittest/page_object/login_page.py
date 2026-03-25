from selenium import webdriver
from Day11.pom_unittest.base_page.base_page import BasePage


class LoginPage(BasePage):
    # 页面url
    url = 'http://39.101.122.147:3000/user/login'

    # 页面核心元素：与操作流程相关联的元素，其余元素不需要。
    login_name = ('id', 'loginName')  # 元素核心内容包括定位方法以及对应的value
    login_pwd = ('id', 'password')
    login_code = ('id', 'inputCode')
    login_img = ('xpath', '//img[@data-v-4f5798c5]')
    login_button = ('xpath', '//button[@data-v-4f5798c5]')

    # 页面的子流程封装
    def login(self, user, pwd):
        self.open_url(self.url)
        self.input(*self.login_name, text=user)
        self.input(*self.login_pwd, text=pwd)
        self.input(*self.login_code, text=self.get_code(*self.login_img))
        self.click(*self.login_button)
        self.wait(15)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = LoginPage(driver)
    lp.login('jsh', '123456')
