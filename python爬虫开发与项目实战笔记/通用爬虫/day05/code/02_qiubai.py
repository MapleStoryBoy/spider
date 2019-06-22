# coding=utf-8
import requests
from lxml import etree

class QiubaiSpdier:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"

        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1,14)]

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode()

    def get_content_list(self,html_str): #提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div")  #分组
        content_list = []
        for div in div_list:
            item= {}
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = [i.replace("\n","") for i in item["content"]]
            item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class")
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon","") if len(item["author_gender"])>0 else None
            item["auhtor_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item["auhtor_age"] = item["auhtor_age"][0] if len(item["auhtor_age"])>0 else None
            item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item["content_img"] = "https:"+item["content_img"][0] if len(item["content_img"])>0 else None
            item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["author_img"] = "https:"+item["author_img"][0] if len(item["author_img"])>0 else None
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self,content_list): #保存
        for i in content_list:
            print(i)

    def run(self): #实现主要逻辑
        #1.url_list
        url_list = self.get_url_list()
        #2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            #3.提取数据
            content_list = self.get_content_list(html_str)
            #4.保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai = QiubaiSpdier()
    qiubai.run()