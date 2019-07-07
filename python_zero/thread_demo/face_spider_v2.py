#encoding: utf-8

import threading
import requests
from lxml import etree
from urllib import request
import os
import re
from queue import Queue

class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue


    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url,headers=self.headers)
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
            self.img_queue.put((img_url,img_name))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer, self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty():
                if self.page_queue.empty():
                    return
            img = self.img_queue.get(block=True)
            url,filename = img
            request.urlretrieve(url,'images/'+filename)
            print(filename+'  下载完成！')

def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1,101):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue,img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()