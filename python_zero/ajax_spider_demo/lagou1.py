#encoding: utf-8

import requests
from lxml import etree
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    "Referer": 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    "Cookie": 'user_trace_token=20171206163541-71593465-da60-11e7-8605-525400f775ce; LGUID=20171206163541-715939f9-da60-11e7-8605-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=141; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAGGABCBF9D054E9D5CD20438137EE72BA670F77; TG-TRACK-CODE=jobs_code; SEARCH_ID=6948b92f168c467abbfc22088e9e75ed; _gid=GA1.2.1756665935.1512549342; _ga=GA1.2.1847536113.1512549342; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512713752,1512717353,1512722886,1512725799; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512729162; LGSID=20171208164805-81efd6b1-dbf4-11e7-9c6f-5254005c3644; LGRID=20171208183242-1f27416f-dc03-11e7-9c6f-5254005c3644',
    'Origin': 'https://www.lagou.com',
    "X-Anit-Forge-Code": "0",
    "X-Anit-Forge-Token": "None",
    'X-Requested-With': "XMLHttpRequest"
}

def request_list_page():
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    data = {
        'first': "false",
        'pn': 1,
        'kd': 'python'
    }
    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data)
        # json方法：如果返回来的是json数据。那么这个方法会自动的load成字典
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' % positionId
            parse_postion_detail(position_url)
            break
        break

def parse_postion_detail(url):
    response = requests.get(url,headers=headers)
    text = response.text
    html = etree.HTML(text)
    position_name = html.xpath("//span[@class='name']/text()")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r"[\s/]","",city)
    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]","",work_years)
    education = job_request_spans[3].xpath(".//text()")[0].strip()
    education = re.sub(r"[\s/]","",education)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    print(desc)


def main():
    request_list_page()

if __name__ == '__main__':
    main()