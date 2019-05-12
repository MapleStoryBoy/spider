#属性多值匹配,需要使用contains函数
from lxml import etree

text = '''
    <li class="li li-first"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"li")]/a/text()')
print(result)

#多属性匹配
text2 = '''
    <li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html2 = etree.HTML(text2)
result2 = html2.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')
print(result2)


