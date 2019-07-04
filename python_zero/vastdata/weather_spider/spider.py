#encoding: utf-8

import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

# pyecharts
# pip install pyecharts

ALL_DATA = []

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    text = response.content.decode('utf-8')
    # html5lib
    # pip install html5lib
    # lxml：C语言写的
    soup = BeautifulSoup(text,'html5lib')
    conMidtab = soup.find('div',attrs={"class":"conMidtab"})
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index,tr in enumerate(trs):
            tds = tr.find_all("td")
            # 如果是第0个城市，那么城市名是放在第1个td标签下
            # 如果是后面的城市（不是第0个城市），那么城市名是放在第0个td标签下
            if index == 0:
                city_td = tds[1]
            else:
                city_td = tds[0]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city':city,"min_temp":int(min_temp)})
            # print({"city":city,"min_temp":int(min_temp)})

if __name__ == '__main__':
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml',
    ]
    for url in urls:
        get_page(url)

    ALL_DATA.sort(key=lambda x:x['min_temp'])

    cities = []
    temps = []
    for x in range(0,10):
        value = ALL_DATA[x]
        city = value['city']
        min_temp = value['min_temp']
        cities.append(city)
        temps.append(min_temp)

    chart = Bar("中国天气最低温度排行榜")
    chart.add("",cities,temps)
    chart.render('temperature.html')