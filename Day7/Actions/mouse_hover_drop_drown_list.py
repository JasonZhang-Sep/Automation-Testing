from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = 'https://www.baidu.com'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(5)

# 鼠标悬停在“设置”上
ActionChains(driver).move_to_element(
    WebDriverWait(driver, 10, 0.5).until(
        EC.presence_of_element_located(('xpath', '//span[@id="s-usersetting-top"]'))
    )
).perform()

# 点击“高级搜索”
driver.find_element('xpath','//span[text()="高级搜索"]').click()
sleep(2)

# 点击下拉框
driver.find_element('xpath', '//div[@class="c-select adv-gpc-select"]').click()
# 点击下拉框的选项
driver.find_element('xpath', '//p[text()="一天内"]').click()

sleep(2)




