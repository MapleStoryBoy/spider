# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("https://www.bilibili.com/v/kichiku/mad/#/all/stow")

print(driver.find_element_by_xpath("//ul[@class='vd-list mod-2']/li//a[@class='title']").text)

#翻页
driver.find_element_by_xpath("//button[@class='nav-btn iconfont icon-arrowdown3']").click()

time.sleep(3)
print(driver.find_element_by_xpath("//ul[@class='vd-list mod-2']/li//a[@class='title']").text)

driver.quit()