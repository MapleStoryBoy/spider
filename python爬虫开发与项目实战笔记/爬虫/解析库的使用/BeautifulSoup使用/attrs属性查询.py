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
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))


#find()返回单个元素
'''
find_parents()和find_parent(): 前者返回所有祖先节点， 后者返回直接父节点。
find_next_siblings()和find_next_sibling(): 前者返回后面所有的兄弟节点 ， 后者返回后面
第一个兄弟节点 。
find_previous_siblings()和find_previous_sibling(): 前者返回前面所有的兄弟节点， 后者
返回前面第一个兄弟节点 。
find_all_next()和 find_next(): 前者返回节点后所有符合条件的节点，后者返回第一个符合 条件的节点 。
find_all_previous()和 find_previous():前者返回节点后所有符合条件的节点，后者返回第 一个符合条件的节点 。

'''
