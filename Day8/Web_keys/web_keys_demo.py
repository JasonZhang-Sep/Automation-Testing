from web_keys import WebKeys

driver = WebKeys('chrome')
driver.open_url('https://www.baidu.com/')
driver.maximize_window()
driver.implicitly_wait(5)
driver.input('id', 'chat-textarea', 'python')
driver.click('id', 'chat-submit-button')
driver.assert_text('xpath', '//span[text()="Python官网"]', 'Python官网')
driver.wait(5)
driver.close()