# -*- coding: utf-8 -*-
import scrapy
from tieba.items import TiebaItem



class TiebaStlSpider(scrapy.Spider):
    name = 'tieba_stl'
    allowed_domains = ['tieba.baidu.com']
    # start_urls = ['https://tieba.baidu.com/f?kw=英文花体字']
    start_urls = ['http://tieba.baidu.com/mo/q---596A8CA33D57134A7383E14E264D8288%3AFG%3D1--1-3-0--2--wapp_1516511596154_469/m?pnum=1&lm=&tnum=988&kw=%E8%8B%B1%E6%96%87%E8%8A%B1%E4%BD%93%E5%AD%97&lp=5009&pinf=1_2_0&sub=%E8%B7%B3%E9%A1%B5']

    def parse(self, response):
        # 分组获取每个帖子
        tz_list = response.xpath("//div[contains(@class, 'i')]")
        print("-"*100 , tz_list)
        # 遍历取到的li标签, 取出相应信息
        for div in tz_list:
            item = TiebaItem()
            item['tz_href'] = 'https://tieba.baidu.com' + div.xpath(".//a/@href").extract_first()
            item['tz_title'] = div.xpath(".//a/text()").extract()
            # print("*"*100, item)
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={"item":item}
            )

        # 下一页
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                'http://tieba.baidu.com/mo/q---596A8CA33D57134A7383E14E264D8288%3AFG%3D1--1-3-0--2--wapp_1516511596154_469' + next_url,
                callback=self.parse
            )

    # 处理每个帖子详情信息
    def parse_detail(self, response):
        item = response.meta['item']
        div_list = response.xpath("//div[@class='i']")
        for div in div_list:
            # item['tz_visitor_response'] = div.xpath(".//div[@class='i']/text()").extract()
            item['tz_img'] = div.xpath(".//img[@class='BDE_Image']/@href").extract_first()
            item['tz_talk'] = div.xpath(".//span[@class='lzl_content_main']/text()").extract()

            yield item

        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                'https://tieba.baidu.com' + next_url,
                callback=self.parse_detail
            )
