from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://www.baidu.com'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# 上传文件操作
# file = r'D:\桌面\Reassignment\图像.png'
# driver.find_element('xpath', '//span[@class="soutu-btn"]').click()
# driver.find_element('xpath', '//input[@value="上传图片"]').send_keys(file)

driver.find_element('xpath', '//*[@id="chat-textarea"]').send_keys('分布式部署')
driver.find_element('xpath', '//*[@id="chat-submit-button"]').click()
# 显示等待的两种写法
# WebDriverWait(driver, 10, 0.5).until(lambda element:
#                                      driver.find_element(
#                                          ('XPATH', '//span[text()="(数据分散存储的技术) - 百度百科"]')),
#                                      message='未找到元素'
#                                      )

WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.XPATH, '//span[text()="(数据分散存储的技术) - 百度百科"]')),
    message='未找到元素'
).click()

handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[0])

# 新建一个标签页，访问163邮箱
driver.switch_to.new_window('tab')
driver.get('https://mail.163.com/')

# 新建一个窗口，访问京东
driver.switch_to.new_window('window')
driver.get('https://www.jd.com/')

sleep(5)
