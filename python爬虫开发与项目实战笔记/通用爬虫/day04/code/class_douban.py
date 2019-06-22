#  _*_coding: utf-8 _*_
import json
import requests
from parse_url import parse_url
import sys
from pprint import pprint
import re


class douban:
    def __init__(self, url):
        self.url = url
        self.L_url = []
        self.start = 0
        self.html_str = ""
        self.ret = {}

    def get_total(self):
        html_str = parse_url(self.url)
        # json.loads把json字符串转化为python类型
        ret1 = json.loads(html_str)
        total = ret1["total"]
        return total

    def get_url(self, total):
        while self.start < total + 50:
            url = self.url.format(
                self.start + 1, 50)
            self.L_url.append(url)
            self.start += 50

    def get_name(self):
        Wurl = self.url
        reg = r'https://m.douban.com/rexxar/api/v2/subject_collection/(.*?)/'
        name = re.findall(reg, Wurl)
        return name[0] + ".json"

    def data(self, name):
        for url in self.L_url:
            self.html_str = parse_url(url)
            ret = json.loads(self.html_str)
            with open(name, "a", encoding="utf-8") as f:
                f.write(json.dumps(ret, ensure_ascii=False, indent=4))

    def run(self):
        total = self.get_total()
        self.get_url(total=total)
        name = self.get_name()
        self.data(name=name)


if __name__ == '__main__':
    url_dict = {
        "美国": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&start=0&count=18&loc_id=108288",
        "英国": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?os=android&start=0&count=18&loc_id=108288",
        "韩国": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_korean_drama_hot/items?os=android&start=0&count=18&loc_id=108288",
        "中国": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?os=android&start=0&count=18&loc_id=108288"
    }
    Len = len(sys.argv)
    for i in range(Len - 1):
        url_name = sys.argv[i + 1]
        url = url_dict[url_name]
        print(url)
        douban = douban(url)
        douban.run()
