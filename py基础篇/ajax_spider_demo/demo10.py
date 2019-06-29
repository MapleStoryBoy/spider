#encoding: utf-8

from selenium import webdriver

driver_path = r"D:\ProgramApp\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://60.17.239.207:31032")

driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)

driver.get("http://httpbin.org/ip")


