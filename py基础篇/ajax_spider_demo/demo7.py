#encoding: utf-8

from selenium import webdriver

driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com/')

# driver.get("https://www.douban.com/")
driver.execute_script("window.open('https://www.douban.com/')")
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])

print(driver.current_url)
print(driver.page_source)

# 虽然在窗口中切换到了新的页面。但是driver中还没有切换。
# 如果想要在代码中切换到新的页面，并且做一些爬虫。
# 那么应该使用driver.switch_to_window来切换到指定的窗口
# 从driver.window_handlers中取出具体第几个窗口
# driver.window_handlers是一个列表，里面装的都是窗口句柄。
# 他会按照打开页面的顺序来存储窗口的句柄。