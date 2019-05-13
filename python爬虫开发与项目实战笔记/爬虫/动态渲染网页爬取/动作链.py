'''
实现一个节点的拖曳操作，将某个节点从一处拖曳到另外一处
'''
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)

browser.switch_to.frame('iframeResult')
source = browser.find_elements_by_css_selector('#draggable')
target = browser.find_elements_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source,target)
actions.perform()


'''
首先，打开网页中的一个拖曳实例 ，然后依次选中要拖曳的节点和拖曳到的目标节点，
接着声明 ActionChains 对象并将其赋值为 actions 变量，然后通过调用actions 
变量的 drag_and_drop()方法， 再调用 perform()方法执行动作，此时就完成了拖曳操作
'''