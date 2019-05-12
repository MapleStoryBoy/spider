from lxml import etree
text = '''
<div>
<Ul>
<li class="item-O"><a href="link1.html">first item</a><li>
<li class="item-1"><a href="link2.html">second item</a><li>
<li class="item-inactive"><a href="link3.html">third item</a></h>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

#所有节点,一般会用刀开头的 XPath规则来选取所有符合要求的节点,*代表匹配所有节点，也就是整个 HTML 文本中的所有节点都会被获取
html = etree.parse('./test.html',etree.HTMLParser())
result = html.xpath('//*')
print(result)

#获取li节点
result1 = html.xpath('//li')
print(result1)
print(result1[0])

#子节点,获取a标签
result2 = html.xpath('//li/a')
print(result2)

#要获取 ul节点 下的所有子孙 a节点，
result3 = html.xpath('//ul/a')
print(result3)

#父节点，知道了子节点，怎样来查 找父节点
result4 = html.xpath('//a[@href="link4.html"]/../@class')
print(result4)
#也可以通过 parent::来获取父节点
result5 = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result5)

#属性匹配
#在选取的时候，我们还可以用@符号进行属性过滤
#如果要选取 class 为 item-1 的 li节点
result6 = html.xpath('//li[@class="item-0"]')
print(result6)

#文本获取
result7 = html.xpath('//li[@class="item-0"]/text()')
print(result7)

#想获取 li 节点内部的文本，就有两种方式，一种是先选取 a 节点再获取文本，另一种就是使用//
result8 = html.xpath('//li[@class="item-0"]/a/text()')
print(result8)

# //匹配
result9 = html.xpath('//li[@class="item-0"]//text()')
print(result9)

#属性获取
result10 = html.xpath('//li/a/@href')
print(result10)











