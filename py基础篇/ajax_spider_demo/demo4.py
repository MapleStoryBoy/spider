#encoding: utf-8

# 常见的表单元素：input type='text/password/email/number'
# buttton、input[type='submit']
# checkbox：input='checkbox'
# select：下拉列表


# 操作输入框
# from selenium import webdriver
# import time
#
# driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.baidu.com/')
#
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
#
# time.sleep(3)
#
# inputTag.clear()


# 操作checkbox
# from selenium import webdriver
# import time
#
# driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('https://www.douban.com/')
#
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()

# 操作select标签：
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
#
# driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driver_path)
# driver.get('http://www.dobai.cn/')
#
# selectBtn = Select(driver.find_element_by_name('jumpMenu'))
# # selectBtn.select_by_index(1)
# # selectBtn.select_by_value("http://m.95xiu.com/")
# selectBtn.select_by_visible_text("95秀客户端")

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')

submitTag = driver.find_element_by_id('su')
submitTag.click()
