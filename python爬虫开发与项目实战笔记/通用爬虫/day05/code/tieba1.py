import os
import re

from lxml import etree

from retrying import retry
import requests

class Tieba():
    def __init__(self):
        self.start_url = "https://tieba.baidu.com/f?ie=utf-8&kw=DOTA2&fr=search"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"}

    @retry(stop_max_attempt_number = 3)
    def _parse_url(self, url):
        response = requests.get(url, headers = self.headers, timeout=8)
        assert response.status_code == 200
        try:
            html_str = response.content.decode()
        except:
            html_str =  response.text
        return html_str

    def parse_url(self, url):
        try:
            html_str = self._parse_url(url)
        except Exception as e:
            print(e)
            html_str = None
        return html_str

    def analysis(self, html_str):
        html_str = re.sub(r'<!--|-->', "", html_str)
        nodes = etree.HTML(html_str)
        title = nodes.xpath('//ul//a[@rel="noreferrer" and @class="j_th_tit "]')
        ret = []  # 这个列表用于保存字典——{ 标题：地址 }
        for t in title:
            temp_dict = dict()
            item = {}
            item["title"] = t.xpath("@title")[0]
            item["href"] = t.xpath("@href")[0] if len(t.xpath("@href"))>0 else None
            item["img_list"] = self.get_pic()
            ret.append(temp_dict)
        return ret

    def get_pic(self, item_list):
        for item in item_list:
            if list(item.values())[0] is None:
                continue
            url = "https://tieba.baidu.com{}".format(list(item.values())[0])
            try:
                html_str = self.parse_url(url)
                html_str = re.sub(r'<!--|-->', "", html_str)
                ret = etree.HTML(html_str)
                pic_list = ret.xpath("//img[]/@src")
                return pic_list
            except Exception as e:
                print(e)
            os.mkdir(list(item.keys())[0])
            for pic in pic_list:
                if pic.startswith("//"):  # 发现贴吧里有的图片是以//开头的，所以需要给这些图片加上http:
                    pic_url = "http:"+ pic
                else:
                    pic_url = pic
                pic_str = requests.get(pic_url, headers=self.headers).content
                if pic_str is not None:
                    pic_rex = re.search(r"(\.jpg|\.png|\.gif)", pic_url)  # 获取图片的格式，是jpg, png 还是gif。
                    if pic_rex is not None:
                        pic_style = pic_rex.group(0)
                    else:
                        pic_style = ".jpg"
                    with open(list(item.keys())[0]+"/"+str(pic_list.index(pic))+ pic_style, "wb") as f:
                        f.write(pic_str)

    def get_next(self, html_str):
        ret = etree.HTML(html_str)
        next_page = ret.xpath('//a[text()="下一页>"]/@href')
        print(next_page)
        return next_page

    def run(self):
        html_str = self.parse_url(self.start_url)
        if html_str is not None:
            # html_str = re.sub(r'<!--|-->', "", html_str)
            item_list = self.analysis(html_str)
            self.get_pic(item_list)
            ret = self.get_next(html_str)
            self.save_ret(ret)
            while len(ret)>0:
                ret[0] = "http:"+ ret[0]
                html_str = self.parse_url(ret[0])
                # html_str = re.sub(r'<!--|-->', "", html_str)
                item_list = self.analysis(html_str)
                self.get_pic(item_list)
                ret = self.get_next(html_str)



if __name__ == '__main__':
    tieba = Tieba()
    tieba.run()