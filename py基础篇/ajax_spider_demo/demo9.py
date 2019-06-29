#encoding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.douban.com/')

# driver.implicitly_wait(20)

element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,'form_email'))
)
print(element)
