#encoding: utf-8

import requests
from bs4 import BeautifulSoup
import json

def get_page():
    # 1. url
    url = "https://movie.douban.com/cinema/nowplaying/changsha/"
    # 2. 请求页面的时候应该发送什么数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    # 3. GET/POST请求
    # 采用的是GET请求

    # 4. 发送请求
    response = requests.get(url, headers=headers)
    text = response.text
    return text

def parse_page(text):
    soup = BeautifulSoup(text,'lxml')
    movies = []
    # data-category=nowplaying
    # attribute
    liList = soup.find_all("li",attrs={"data-category":"nowplaying"})
    for li in liList:
        movie = {}
        title = li['data-title']
        score = li['data-score']
        release = li['data-release']
        duration = li['data-duration']
        region = li['data-region']
        director = li['data-director']
        actors = li['data-actors']
        img = li.find('img')
        thumbnail = img['src']

        movie['title'] = title
        movie['score'] = score
        movie['release'] = release
        movie['duration'] = duration
        movie['region'] = region
        movie['director'] = director
        movie['actors'] = actors
        movie['thumbnail'] = thumbnail
        movies.append(movie)
    return movies

def save_data(data):
    with open('douban.json','w',encoding='utf-8') as fp:
        # json.dump作用：
        # 将字典、列表dump成满足json格式的字符串
        json.dump(data,fp,ensure_ascii=False)


if __name__ == '__main__':
    text = get_page()
    movies = parse_page(text)
    save_data(movies)





