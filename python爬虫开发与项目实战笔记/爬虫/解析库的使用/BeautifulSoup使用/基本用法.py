from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

"""

soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.title.string)

'''
这里首先声明变量 html，它是一个 HTML 字符串 。
但是需要注意的是，它并不是一个完整的 HTML 字符串，
因为 body 和 html 节点都没有闭合 。 接着，我们
将它当作第一个参数传给 BeautifulSoup 对 象，该
对象的第二个参数为解析器的类型(这里使用 lxml)，
此时就完成了 BeaufulSoup对象的初始化。 然后，
将这个对象赋值给 soup变量。
prettify()方法。 这个方法可以把要解析的字符串以标准的缩进格式输出 

'''

#节点选择器---选择元素

print(soup.title)
print(type(soup.title))
print(soup.title . string)
print(soup.head)
print(soup.p)
#提取信息
#获取名称
print(soup.title.name)
#获取属性
print(soup.p.attrs)# attrs 的返回结果是字典形式，它把选择的节点的所有属性和属性值组合成一个字典
print(soup.p.attrs ['name'])
print(soup.p ['name'])
print(soup.p ['class'])

#获取内容
print(soup.p.string)





