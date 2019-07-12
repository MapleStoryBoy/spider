#encoding: utf-8

import requests
from lxml import etree

BASE_DOMAIN = 'http://www.dytt8.net'
HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
'Referer': 'http://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
}

def parse_detail_page(url):
    """
    解析详情页面
    """
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//font[@color='#07519a']//text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
    screenshot = imgs[1]
    movie['cover'] = cover
    movie['screenshoot'] = screenshot

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            year = info.replace("◎年　　代","").strip()
            movie['year'] = year
        elif info.startswith("◎主　　演"):
            # 从当前位置，一直往下面遍历
            actors = [info.replace("◎主　　演","").strip()]
            for x in range(index + 1, len(infos)):
                actor = infos[x]
                if actor.startswith("◎"):
                    break
                actors.append(actor.strip())
            movie['actors'] = actors
    return movie


def get_detail_urls(url):
    resp = requests.get(url, headers=HEADERS)
    text = resp.content.decode('gbk')
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

def spider():
    raw_url = 'http://www.dytt8.net/html/gndy/dyzz/list_23_{page}.html'
    movies = []
    for x in range(1,7):
        url = raw_url.format(page=x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
    print(len(movies))



if __name__ == '__main__':
    spider()