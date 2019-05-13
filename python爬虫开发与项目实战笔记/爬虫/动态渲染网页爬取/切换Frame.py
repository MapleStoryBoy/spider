'''
网页中有一种节点叫作 iframe，也就是子 Frame
Selenium打开页面后，它默认是在父级 Frame里面操作，而此时如果页面中
还有子 Frame，它是不能获取到子 Frame里面的节点的 。 这时就需要使用
switch_to.frame()方法来切 换 Frame。 示例如下:
'''
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:
    print('NO LOGO')

browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

'''
通过 switch_to.frame()方法 w换到子 Frame 里面，然后尝试获取父级 Frame 
里的 logo 节点(这是不能找到的)，如果找不到的话，就会抛出 
NoSuchElementException 异常，异常被捕捉之后，就会输出 NO LOGO。 
接下来，重新切换回父级 Frame, 然后再次重新获取节点，发现此时可以成功获取了 。
'''

