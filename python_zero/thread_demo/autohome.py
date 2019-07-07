#encoding: utf-8

# 汽车之家爬虫

import requests
from lxml import etree
import threading
from queue import Queue
import time
from urllib import request
import os

class AutoHomeThread(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Host': 'car.autohome.com.cn',
        'Cookie': 'fvlid=1512482292556bqJQS1ev; sessionip=110.53.253.128; sessionid=F8CE2ABD-56AD-4A94-BC34-07A82552070F%7C%7C2017-12-05+21%3A58%3A14.497%7C%7C0; ahpau=1; historybbsName4=c-65%7C%E5%AE%9D%E9%A9%AC5%E7%B3%BB; carCookie1111Time=%2C%2C%2C2017/12/5; carCookie1111=0%2C0%2C0%2C1; FromPicList=0; ahpvno=59; CNZZDATA1262640694=616429415-1512485336-https%253A%252F%252Fwww.autohome.com.cn%252F%7C1512485336; Hm_lvt_9924a05a5a75caf05dbbfb51af638b07=1512482295; Hm_lpvt_9924a05a5a75caf05dbbfb51af638b07=1512490262; ref=0%7C0%7C0%7C0%7C2017-12-06+00%3A11%3A03.566%7C2017-12-05+21%3A58%3A14.497; sessionvid=222A9243-759B-4AC7-9C56-C5072BABD451; area=430199; ahrlid=1512490261334IUqW7elTUc-1512490271900; cn_1262640694_dplus=%7B%22distinct_id%22%3A%20%2215f4d0f0de6484-0e51e7febcd48d-c303767-1fa400-15f4d0f0de7bcf%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201512490273%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201512490273%7D%7D; UM_distinctid=15f4d0f0de6484-0e51e7febcd48d-c303767-1fa400-15f4d0f0de7bcf'
    }
    def __init__(self, page_queue, detail_queue, *args, **kwargs):
        super(AutoHomeThread, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.detail_queue = detail_queue
        self.base_domain = "https://club.autohome.com.cn"
        self.session = requests.Session()

class Producer(AutoHomeThread):
    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        print('url:',url)
        response = self.session.get(url,headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        links = html.xpath("//div[@class='uibox']//li//img/@src")
        for link in links:
            img_name = link.split('__')[-1]
            img_url = "https:"+link.replace("t_autohomecar","1024x0_1_q87_autohomecar")
            self.detail_queue.put((img_url,img_name))
            time.sleep(2)

class Consumer(AutoHomeThread):
    def run(self):
        while True:
            img = self.detail_queue.get(timeout=60)
            self.download_image(img)

    def download_image(self,img):
        img_url,img_name = img
        request.urlretrieve(img_url,os.path.join("bmw5",img_name))
        print(img_name+' 下载完成！')

def main():
    page_queue = Queue(20)
    detail_queue = Queue(500)
    urls = [
        'https://car.autohome.com.cn/pic/series/65-1.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-10.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-3.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-12.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-13.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-51.html#pvareaid=2042222',
        'https://car.autohome.com.cn/pic/series/65-14.html#pvareaid=2042222'
    ]
    for url in urls:
        page_queue.put(url)

    for x in range(1):
        t = Producer(page_queue,detail_queue)
        t.start()

    for x in range(1):
        t = Consumer(page_queue,detail_queue)
        t.start()



if __name__ == '__main__':
    main()