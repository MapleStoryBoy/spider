#encoding: utf-8

from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&keywords=python&tid=87&lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=29938&keywords=python&tid=87&lid=2218">22989-金融云高级后台开发</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31236&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐运营开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>2</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31235&keywords=python&tid=87&lid=2218">SNG16-腾讯音乐业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34531&keywords=python&tid=87&lid=2218">TEG03-高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=34532&keywords=python&tid=87&lid=2218">TEG03-高级图像算法研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=31648&keywords=python&tid=87&lid=2218">TEG11-高级AI开发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>4</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32218&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=32217&keywords=python&tid=87&lid=2218">15851-后台开发工程师</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
        <tr class="odd">
            <td class="l square"><a id="test" class="test" target='_blank' href="position_detail.php?id=34511&keywords=python&tid=87&lid=2218">SNG11-高级业务运维工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-24</td>
        </tr>
    </tbody>
</table>
"""


# 1. 获取所有tr标签
# 2. 获取第2个tr标签
# 3. 获取所有class等于even的tr标签
# 4. 将所有id等于test，class也等于test的a标签提取出来。
# 5. 获取所有a标签的href属性
# 6. 获取所有的职位信息（纯文本）

soup = BeautifulSoup(html,'lxml')

# 1. 获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print('='*30)

# 2. 获取第2个tr标签
# tr = soup.find_all('tr',limit=2)[1]
# print(tr)

# 3. 获取所有class等于even的tr标签
# atrribute
# trs = soup.find_all('tr',attrs={'class':"even"})
# for tr in trs:
#     print(tr)
#     print('='*30)

# 4. 将所有id等于test，class也等于test的a标签提取出来。
# aList = soup.find_all('a',id='test',class_='test')
# aList = soup.find_all('a',attrs={"id":"test","class":"test"})
# for a in aList:
#     print(a)

# 5. 获取所有a标签的href属性
# aList = soup.find_all('a')
# for a in aList:
#     # 1. 通过下表操作的方式
#     # href = a['href']
#     # print(href)
#     # 2. 通过attrs属性的方式
#     href = a.attrs['href']
#     print(href)

# 6. 获取所有的职位信息（纯文本）
# trs = soup.find_all('tr')[1:]
# movies = []
# for tr in trs:
#     movie = {}
#     # tds = tr.find_all("td")
#     # title = tds[0].string
#     # category = tds[1].string
#     # nums = tds[2].string
#     # city = tds[3].string
#     # pubtime = tds[4].string
#     # movie['title'] = title
#     # movie['category'] = category
#     # movie['nums'] = nums
#     # movie['city'] = city
#     # movie['pubtime'] = pubtime
#     # movies.append(movie)
#
#     infos = list(tr.stripped_strings)
#     movie['title'] = infos[0]
#     movie['category'] = infos[1]
#     movie['nums'] = infos[2]
#     movie['city'] = infos[3]
#     movie['pubtime'] = infos[4]
#     movies.append(movie)
#
# print(movies)

tr = soup.find_all('tr')[1]
text = tr.string
print(text)