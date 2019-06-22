# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

class RandomUserAgentMiddleware:
    def process_request(self,request,spider):
        ua = random.choice(spider.settings.get("USER_AGENTS_LIST"))
        request.headers["User-Agent"] = ua


class CheckUserAgent:
    def process_response(self,request,response,spider):
        # print(dir(response.request))
        print(request.headers["User-Agent"])
        return response


