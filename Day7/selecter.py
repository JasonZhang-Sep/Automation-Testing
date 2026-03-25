from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# 通过ID定位
# driver.find_element('id', 'chat-textarea').send_keys('python')
# 通过XPATH定位
# driver.find_element('xpath', '//*[@id="chat-textarea"]').send_keys('python')

# driver.find_element('xpath', '//*[contains(text(),"新闻")]').click()
# <a>标签可通过link text和partial link text属性定位
# driver.find_element('link text', "新闻").click()
driver.find_element('partial link text', "新闻").click()

# 通过id,xpath和contains() 定位百度一下button
# driver.find_element('id', 'chat-submit-button').click()
# driver.find_element('xpath', '//*[@id="chat-submit-button"]').click()
# driver.find_element('xpath', '//button[contains(text(), "百度一下")]').click()


sleep(5)
