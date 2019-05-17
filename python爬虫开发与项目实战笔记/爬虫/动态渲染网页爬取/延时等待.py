
#隐式等待,implicitly_wait()方法实现了隐式等待

'''
使用隐式等待执行测试的时候，如果 Selenium没有在 DOM 中找到节点，
将继续等待，超出设 定时间后，则抛什1找不到节点的异常。 换句话说，
当查找节点而节点并没有立即出现的时候，隐式等 待将等待一段时间再查找
DOM，默认的时间是 0
'''

from selenium import webdriver

browser = webdriver.Chrome()

browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)






















