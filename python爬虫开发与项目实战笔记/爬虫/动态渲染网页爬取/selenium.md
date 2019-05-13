- 声明浏览器对象
    Selenium支持非常多的浏览器，如 Chrome、 Firefox、 Edge等 ，还有
    Android、 Black.Berry等手机端的浏览器，另外，也支持无界面浏览器 PhantomJS。
    - 可以用如下方式初始化 
        - from selenium import webdriver
        - browser = webdriver.Chrome() 
        - browser = webdriver.Firefox() 
        - browser = webdriver.Edge() 
        - browser = webdriver.PhantomJS() 
        - browser = webdriver.Safari()
        - 这样就完成了浏览器对象的初始化并将其赋值为browser对象。
- 访问页面
    - 用get()方法来请求网页，参数传入链接URL
    - 代码：
    
    
        from selenium import webdriver
        browser = webdriver.Chrome()
        browser.get('https://www.baidu.com')
        print(browser.page_source)
        browser.close()
- 查找节点
    - 单个节点
        - find_element_by_name()根据name值获取
        - find_element_by_id()是根据id获取
        - 还有可以根据XPath、CSS选择器等获取方式
        - find_element_by_link_text
        - find_element_by_partial_link_text
        - find_element_by_tag_name
        - find_element_by_class_name
        - find_element_by_css_selector
        - 实例：
        
        
        from selenium import webdriver
        browser = webdriver.Chrome()
        browser.get('https://www.taobao.com')
        input_first = browser.find_element_by_id('q')
        input_second = browser.find_element_by_css_selector('#q')
        input_three = browser.find_element_by_xpath('//*[@id="q"]')
        print(input_first,input_second,input_three)
        browser.close()
        
- 多个节点
    - 需要用 find_elements()
    
- 节点交互
    - Selenium可以驱动浏览器来执行一些操作，也就是说可以让浏览器模拟执行一些动作 。 
        比较常见 的用法有:输入文字时用 send_keys()方法，清空文字时用 clear()方法，
        点击按钮时用 click()方法
    - 实例：见节点交互.py
        
- 执行JavaScript
    - 使用execute_script方法
     
- 获取节点信息
    - 获取属性  
        - 使用 get_attribute()方法来获取节点的属性
        - 实例：见获取属性.py    
 
        
        
            
        
    