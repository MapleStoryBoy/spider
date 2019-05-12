html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')

#select方法
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
print(type(soup.select('ul')[0]))

#嵌套选择，select()方法同样支持嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))

    #获取属性，尝试获取每个 ul节点的 id属性:
    print(ul['id'])
    print(ul.attrs['id'])

#获取文本
for li in soup.select('li'):
    print('Get Text:',li.get_text())
    print('String:',li.string)





