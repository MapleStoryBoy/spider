#encoding: utf-8

import requests
from lxml import etree
from urllib import request
import os
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}

def parse_page(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//a//img")
    for img in imgs:
        if img.get('class') == 'gif':
            continue
        img_url = img.xpath(".//@data-original")[0]
        suffix = os.path.splitext(img_url)[1]
        alt = img.xpath(".//@alt")[0]
        alt = re.sub(r'[，。？?,/\\·]','',alt)
        img_name = alt + suffix
        request.urlretrieve(img_url,'images/'+img_name)
        print(img_name+'下载完毕！')

def main():
    for x in range(1,101):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        parse_page(url)
        break

if __name__ == '__main__':
    main()