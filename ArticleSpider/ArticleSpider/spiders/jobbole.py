# -*- coding: utf-8 -*-
import scrapy
import re,time
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import JobBoleArticleItem
from ArticleSpider.utils.common import get_md5


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        '''
        1，获取文章列表页中的文章url并交给解析函数进行具体字段的解析
        2，获取下一页的url并交给scrapy进行下载，下载完成后交给parse函数
        '''
        # 解析列表页中的所有文章url交给解析函数进行具体字段的解析
        post_nodes = response.css("#archive .floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first('')
            post_url = post_node.css("::attr(href)").extract_first('')
            #url拼接好后使用yield关键字返回给scrapy进行下载
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":image_url},callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        time.sleep(1)
        next_url = response.css(".next.page-numbers::attr(href)").extract_first('')
        if next_url:
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse)

    def parse_detail(self,response):
        '''
        处理每个url的方法，解析具体文章的逻辑
        提取文章的具体字段
        '''
        article_item = JobBoleArticleItem()
        #文章封面图
        front_image_url = response.meta.get('front_image_url','')
        #提取文章标题
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        #提取日期
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·','')
        #提取点赞数目
        praise_nums = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        #提取收藏数目（^(\d)* 匹配任意数字
        fav_nums = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0].strip()
        match_re = re.match(r'^(\d)*',fav_nums)
        if match_re:
            fav_nums = match_re.group()
        else:
            fav_nums = 0
        #提取文章评论数
        #comment = response.xpath('//a[@href="#article-comment"]/text()').extract()[0].strip()
        comment = response.css('a[href="#article-comment"] span::text').extract()[0].strip()
        match_re = re.match(r'^(\d)*',comment)
        if match_re:
            comment = match_re.group()
        else:
            comment = 0
        #提取网页文章的内容
        content = response.xpath('//div[@class="entry"]').extract()[0]
        #这一步主要为了提取文章的所属类型
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ','.join(tag_list)

        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        article_item["create_date"] = create_date
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = praise_nums
        article_item["fav_nums"] = fav_nums
        article_item["comment"] = comment
        article_item["tags"] = tags
        #article_item["content"] = content
        yield article_item


        #print(title,create_date,praise_nums,fav_nums,comment,tags,front_image_url)

