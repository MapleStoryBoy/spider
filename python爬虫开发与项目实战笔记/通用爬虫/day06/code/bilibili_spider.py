#  _*_ coding: utf-8 _*_
import requests, re
from lxml import etree

class BlBl:
    def __init__(self,url):
        self.url = url
        # 哔哩哔哩弹幕url
        self.danmu_url= 'https://comment.bilibili.com/{}.xml'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get_html(self,url):
        """发送请求,返回响应"""
        return requests.get(url,headers = self.headers).content.decode()

    def save_danmu(self, l,num):
        """保存弹幕"""
        print('保存')
        with open('./danmu/{}.txt'.format(num), 'a') as f:
            for danmu_str in l:
                print(danmu_str)
                f.write(danmu_str)
                f.write("\n")

    def get_xml(self,li):
        print(li)
        for num in li:  # 遍历cid列表,设置弹幕请求url
            # 拼接弹幕url,调用函数,发送请求,获取结果
            danmu_xml = self.get_html(self.danmu_url.format(num)).encode()  # 解析时说有问题,encode()转为byte型
            # 将获取到的xml类型转换为etree对象
            xml_etr_obj = etree.HTML(danmu_xml)
            # 获取弹幕列表
            l = xml_etr_obj.xpath('//d/text()')  # # 解析时说有问题,获取结果是用encode()转为byte型
            print('准备保存')
            self.save_danmu(l,num)  # 保存

    def run(self):
        # 发送请求,获取结果
        bl_html = self.get_html(self.url)
        print('正则获取cid')
        # 提取此套的所有网页url_地址和cid
        li = re.findall(r"<option value='.*?' cid='(\d+)'>",bl_html)
        if len(li) == 0:  # 如果只有一个视频,上边这个列表为空,获取单个cid
            li = re.findall(r"EmbedPlayer\('player',.*?cid=(\d+)&aid",bl_html)
        # 请求xml的url并保存弹幕
        self.get_xml(li)

if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av18198653/'
    bili = BlBl(url)
    bili.run()