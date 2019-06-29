#encoding: utf-8

import requests
import time
from lxml import etree
import re

def request_lagou():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Cookie': 'user_trace_token=20171206163541-71593465-da60-11e7-8605-525400f775ce; LGUID=20171206163541-715939f9-da60-11e7-8605-525400f775ce; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=141; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAIAACBIA5E737E082B1D6BF31045754DEFA10AA; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; TG-TRACK-CODE=index_search; SEARCH_ID=3a36bed3f739481a8528527b46a843c3; _ga=GA1.2.1847536113.1512549342; _gid=GA1.2.1756665935.1512549342; LGSID=20171208164805-81efd6b1-dbf4-11e7-9c6f-5254005c3644; LGRID=20171208164809-845c73aa-dbf4-11e7-9c6f-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512648813,1512713752,1512717353,1512722886; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512722890',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Origin': 'https://www.lagou.com'
    }
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
    data = {
        'first': "false",
        'pn': 2,
        'kd': "python"
    }
    for x in range(1,10):
        data['pn'] = x
        response = requests.post(url, headers=headers, data=data)
        positions = response.json()["content"]["positionResult"]["result"]
        for position in positions:
            position_url = "https://www.lagou.com/jobs/%s.html" % position['positionId']
            position_resp = requests.get(position_url,headers=headers)
            parse_position(position_resp.text)
            time.sleep(1)

def parse_position(source):
    html = etree.HTML(source)
    try:
        title = html.xpath("//span[@class='name']/text()")[0]
        company = html.xpath("//h2[@class='fl']/text()")[0].strip()
        job_request_span = html.xpath("//dd[@class='job_request']//span")
        salary = job_request_span[0].xpath(".//text()")[0]
        salary = salary.strip()
        city = job_request_span[1].xpath(".//text()")[0]
        city = re.sub(r"[/\s]", "", city)
        work_years = job_request_span[2].xpath(".//text()")[0]
        work_years = re.sub(r"[/\s]", "", work_years)
        education = job_request_span[3].xpath(".//text()")[0]
        education = re.sub(r"[/\s]", "", education)
        company_website = html.xpath("//ul[@class='c_feature']/li[last()]/a/@href")[0]
        position_desc = "".join(html.xpath("//dd[@class='job_bt']/div//text()"))
        position = {
            'title': title,
            'city': city,
            'salary': salary,
            'company': company,
            'company_website': company_website,
            'education': education,
            'work_years': work_years,
            'desc': position_desc,
        }
        print(position)
    except:
        print(source)

    print('=' * 40)


def main():
    request_lagou()

if __name__ == '__main__':
    main()
