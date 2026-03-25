from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://mail.qq.com/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)
# 进入第一层iframe
driver.switch_to.frame(driver.find_element('id', 'login_frame'))

# 进入第二层iframe
WebDriverWait(driver, 10, 0.5).until(
    lambda element: driver.find_element('id', 'ptlogin_iframe'),
    message="未找到元素"
)
driver.switch_to.frame(driver.find_element('id', 'ptlogin_iframe'))
driver.find_element('id', 'switcher_plogin').click()

# 返回第一层iframe
driver.switch_to.default_content()
driver.find_element('link text', '基本版').click()

sleep(5)