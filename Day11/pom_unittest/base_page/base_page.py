from time import sleep
import ddddocr


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def open_url(self, url):
        self.driver.get(url)

    # 强制等待
    def wait(self, time_):
        sleep(time_)

    # 定位元素
    def locator(self, by, value):
        return self.driver.find_element(by, value)

    # 输入
    def input(self, by, value, text):
        self.locator(by, value).send_keys(text)

    # 点击
    def click(self, by, value):
        self.locator(by, value).click()

    # 关闭
    def close(self):
        self.driver.close()

    # 退出
    def quit(self):
        self.driver.quit()

    # 文本断言
    def assert_text(self, by, value, expected_text):
        reality = self.locator(by, value).text
        assert reality == expected_text, f'''
        预期结果为：{expected_text}, 实际结果为：{reality}
        {expected_text} ！= {reality}
    '''

    # 获取验证码
    def get_code(self, by, value):
        # 保存验证码为png图片
        file = self.locator(by, value).screenshot_as_png
        # ddddocr实现对验证码内容的识别
        return ddddocr.DdddOcr(show_ad=False).classification(file)
