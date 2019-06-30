
from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get('https:www.baidu.com')

print(driver.page_source)

time.sleep(5)
driver.quit()






