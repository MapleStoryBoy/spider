#encoding: utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

all_data = []

def parse_page(url):
    response = requests.get(url)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.select("div.conMidtab")[0]
    tables = conMidtab.select("table")
    for table in tables:
        trs = table.find_all("tr")[2:]
        for tr in trs:
            city = tr.find_all("a")[0].string
            min_temp = tr.find("td", {"width": "86"}).string
            all_data.append({"city": city, "min_temp": int(min_temp)})
            print({"city": city, "min_temp": int(min_temp)})

def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parse_page(url)

    # 排序
    all_data.sort(key=lambda x:x['min_temp'])

    data = all_data[0:10]
    cities = map(lambda x:x['city'],data)
    temps = map(lambda x:x['min_temp'],data)

    chart = Bar('中国天气最低温度排行榜')
    chart.add('',list(cities),list(temps))
    chart.render('weather.html')

if __name__ == '__main__':
    main()