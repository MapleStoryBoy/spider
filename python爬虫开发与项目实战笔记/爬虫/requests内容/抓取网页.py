
import requests
import re

#构造headers

headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE S.S; Windows NT)'
}

r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)

titles = re.findall(pattern,r.text)
print(titles)








