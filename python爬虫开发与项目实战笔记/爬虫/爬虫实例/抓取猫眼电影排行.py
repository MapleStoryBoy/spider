#抓取首页

import requests,re,json,time
from requests.exceptions import RequestException

def get_one_page(url):
    '''获取第一页电影数据'''
    try:
        #构造headers
        headers = {
            'User-Agent':'Mozilla/4.0 (compatible; MSIE S.S; Windows NT)',

        }
        #response请求
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    #正则匹配获取页面数据
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>'
        '.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(pattern,html)
    #遍历提取结果并生成字典
    for item in items:
        # 把当前的元素记下来，保存在集合中，循环结束后将返回该集合
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score':item[5].strip() + item[6].strip()
        }


def write_to_file(content):
    '''写入文件，保存爬取数据'''
    with open('result.txt','a',encoding='utf-8') as f:
        print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    # 获取前十页电影的offset值
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)








