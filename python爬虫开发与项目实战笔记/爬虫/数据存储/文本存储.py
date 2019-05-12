

import requests
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"

headers = {
    "User-Agent":'Mozilla/4.0 (compatible; MSIE S.S; Windows NT)',
}

html = requests.get(url,headers=headers).text

doc = pq(html)

items = doc('.explore-tab .feed-item').items()
for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    file = open('explore.txt','a',encoding='utf-8')
    file.write('\n'.join([question,author,answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()














