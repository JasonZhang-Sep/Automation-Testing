from selenium import webdriver


def option_func():
    option = webdriver.ChromeOptions()
    # 页面加载策略
    # option.page_load_strategy = 'normal'
    # 页面最大化
    option.add_argument('start-maximized')
    # 去掉黄条警告
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 无头模式
    # option.add_argument('--headless')
    # 账号密码的弹窗屏蔽
    prefs = {
        'credentials_enable_service': False,
        'profile.password_manager_enable': False
    }
    option.add_experimental_option('prefs', prefs)

    # 去除控制台的多余日志信息。
    # option.add_experimental_option('excludeSwitches', ['enable-logging'])
    # # # 如果常规日志去除无效果，则可以调用以下方法
    # option.add_argument('--log_level=3')
    # option.add_argument('--disable-gpu')
    # option.add_argument('--ignore-certificate-errors')

    return option

