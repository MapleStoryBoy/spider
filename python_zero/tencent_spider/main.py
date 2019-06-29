#encoding: utf-8

# 腾讯招聘网爬虫作业

from lxml import etree
import requests

BASE_DOMAIN = "http://hr.tencent.com/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Cookie": "ts_refer=www.baidu.com/link; pgv_pvid=6696594441; ts_uid=3711980616; PHPSESSID=npfgl3krhdbvp369bcdqlnmof5",
    "Host": "hr.tencent.com",
    "Upgrade-Insecure-Requests":"1"
}

def parse_detail_page(url):
    position = {}
    response = requests.get(url,headers=HEADERS)
    html = etree.HTML(response.text)
    title = html.xpath("//td[@id='sharetitle']/text()")[0]
    tds = html.xpath("//tr[@class='c bottomline']/td")
    address = tds[0].xpath(".//text()")[1]
    category = tds[1].xpath(".//text()")[1]
    nums = tds[2].xpath(".//text()")[1]
    more_infos = html.xpath("//ul[@class='squareli']")
    duty = more_infos[0].xpath(".//text()")
    require = more_infos[1].xpath(".//text()")

    position['title'] = title
    position['address'] = address
    position['category'] = category
    position['nums'] = nums
    position['duty'] = duty
    position['require'] = require
    return position


def get_detail_urls(url):
    response = requests.get("http://hr.tencent.com/position.php?lid=&tid=&keywords=python&start=0",headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    links = html.xpath("//tr[@class='even' or @class='even']//a/@href")
    links = map(lambda url:BASE_DOMAIN+url,links)
    return links

def spider():
    base_url = "http://hr.tencent.com/position.php?lid=&tid=&keywords=python&start={}"
    positions = []
    for x in range(0,43):
        x *= 10
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            position = parse_detail_page(detail_url)
            positions.append(position)
            print(position)
    # print(positions)

if __name__ == '__main__':
    spider()