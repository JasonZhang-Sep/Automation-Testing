from time import sleep
import ddddocr
from selenium import webdriver
from Day8.Options.options import option_func


# 创建浏览器对象
def open_browser(type_):
    # try:
    #     if type_ == 'chrome':
    #         driver = webdriver.Chrome(options=option_func())
    #     else:
    #         driver = getattr(webdriver, type_.capitalize())()
    #
    # except:
    #     driver = webdriver.Chrome()
    # return driver

    # 浏览器映射关系
    browser = {
        'Chrome': ['谷歌浏览器', '谷歌', 'chrome', 'CHROME'],
        'Firefox': ['火狐浏览器', '火狐', 'firefox', 'FIREFOX'],
        'Edge': ['Edge浏览器', 'edge', 'EDGE'],
        'Safari': ['Safari浏览器', 'safari', 'SAFARI'],
    }
    try:
        # 遍历映射关系查找匹配项
        for key, value in browser.items():
            if type_ in value:
                driver = getattr(webdriver, key)()
                return driver
        # 若未匹配到任何浏览器，尝试使用Chrome浏览器
        driver = webdriver.Chrome()
        return driver
    except Exception as e:
        # 捕获异常并记录日志
        print(f"启动浏览器失败: {e}")
        raise RuntimeError(f"无法启动指定浏览器 '{type_}'，请检查配置或依赖是否正确") from e


class WebKeys:
    def __init__(self, type_):
        self.driver = open_browser(type_)
        self.driver.implicitly_wait(5)

    # 访问url
    def open_url(self, url):
        self.driver.get(url)

    # 最大化窗口
    def maximize_window(self):
        self.driver.maximize_window()

    # 隐式等待
    def implicitly_wait(self, time):
        self.driver.implicitly_wait(time)

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
        预期结果为:{expected_text}, 实际结果为:{reality}
        {expected_text}!={reality}
'''

    # 获取验证码
    def get_code(self, by, value):
        # 保存验证码为png图片
        file = self.locator(by, value).screenshot_as_png
        # ddddocr实现对验证码内容的识别
        return ddddocr.DdddOcr(show_ad=False).classification(file)

