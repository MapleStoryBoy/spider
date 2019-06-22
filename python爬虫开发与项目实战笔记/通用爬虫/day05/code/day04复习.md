### 正则如何进行非贪婪匹配，在div标签中的数据如何通过正则取出来
- `*?` `+?`
- `re.findall("<div class="a">.*?<div id="">(.*?)</div>",str)` 返回列表，没有匹配到就是空列表

### xpath如何获取文本，如何获取任意标签下的文本
- `a/text()` 只能获取a下的文本
- `a//text()` 能够获取a下的和a包含的标签的文本
- `a[text()="下一页"]`

### xpath如何获取属性，如何对标签进行定位
- `a/@href`
- `div[@class='b']`

### xpath中//有什么用
- `//自最前面的时候，表示html中任意位置开始选择`
- `div//*  放在节点后面的时候，能够选择当前节点下的所有的标签`

### xpath获取某一个或者某几个
- `//a[1]` 第一个
- `//a[last()]` 最后一个
- `//a[position()<=3]`
- `//a[1]|//a[3]`

### lxml如何如何使用，如何把lxml处理之后的内容转化为字符串
- from lxml import etree
- element = etree.HTML(bytes、str) #把字符串转化为element对象
- etree.tostring(element) #把element对象转化为字符串
- element.xpath("xpath_str")
