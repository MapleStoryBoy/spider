### selenium 如何使用
- from selenium import webdriver
- driver = webdriver.Chrome()
- driver.get(url)
- driver.quit()

### selenium如何定位，如何获取属性和文本
- driver.find_element  返回一个对象，没有会报错
- driver.find_elements 返回一个列表，空列表
- driver.find_element_by_id()
- driver.find_element_by_class_name()
- driver.find_element_by_xpath()
- driver.find_element_by_link_text()
- driver.find_element_by_id().text
- driver.find_element_by_id().get_attribute()

### selenium如何切换iframe中
- driver.switch_to.frame(frame的id,name,driver.find_element_by_xpath("//a[1]"))

### 遇到验证码如何处理
- url地址对应的验证码会变
  - 1.实例化一个session
  - 2.session请求登录页面，获取验证码的地址
  - 3.session请求验证码，识别
  - 4.session发送post请求
- url地址对应的验证码不会变
  - 请求验证码地址，识别
