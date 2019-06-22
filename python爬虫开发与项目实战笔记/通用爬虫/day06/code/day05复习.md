### lxml模块如何使用
- from lxml import etree
- element = etree.HMTL(str,bytes)
- element.xpath("xpath")
- etree.tostring(element) #把element转化为字符串


### xpath有哪些常用方法
- `//` 从任意位置选择节点
  - `//a/text()` a下的文本
  - `//a//text()` a下所有的文本
- `.` 当前路径
- `@符号`
  - `a/@href`
  - `div[@class='a']`
- `text()`
  - `a[text()='下一页']`
- `..` 上一级
- `//a[1]`
- `//a[last()]`
- `//a[postion()<4]`
- `//a[1]|//a[5]`
- `a[contains(text(),"下一页")]`

### queue模块如何使用
- from queue import Queue
- 实例化
- queue.put() #get计数减一
- queue.get()
- queue.task_doen() #计数减一
- queue.join() #让主线程阻塞
