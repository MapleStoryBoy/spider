
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scollHeight)')
browser.execute_script('alert("To Bottom")')

'''
利用 execute script()方法将进度条下拉到最底部，然后弹H\ alert提示框
'''












