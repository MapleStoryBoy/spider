#encoding: utf-8

import requests
from bs4 import BeautifulSoup
import json

# 1. 将目标网站上的页面抓取下来
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    'Referer': 'https://movie.douban.com/'
}
url = 'https://movie.douban.com/cinema/nowplaying/changsha/'
response = requests.get(url,headers=headers)
text = response.text
# print(response.text)
# response.text：返回的是一个经过解码后的字符串，是str（unicode）类型
# response.content：返回的是一个原生的字符串，就是从网页上抓取下来的，没有经过处理的字符串，是bytes类型


# 2. 将抓取下来的数据根据一定的规则进行提取
soup = BeautifulSoup(text,'lxml')
all_li = soup.find_all('li',attrs={"data-category":"nowplaying"})
movies = []
for li in all_li:
    movie = {}
    title = li['data-title']
    score = li['data-score']
    release = li['data-release']
    duration = li['data-duration']
    region = li['data-region']
    director = li['data-director']
    actors = li['data-actors']
    category = li['data-category']
    img = li.find("img")
    thumbnail = img['src']

    movie['title'] = title
    movie['score'] = score
    movie['release'] = release
    movie['duration'] = duration
    movie['region'] = region
    movie['director'] = director
    movie['actors'] = actors
    movie['category'] = category
    movie['thumbnail'] = thumbnail

    movies.append(movie)

with open('douban.json','w',encoding='utf-8') as fp:
    json.dump(movies,fp,ensure_ascii=False)

