#encoding: utf-8

# 大鹏董成鹏主页：http://www.renren.com/880151247/profile
# 人人网登录url：http://www.renren.com/PLogin.do

from urllib import request
from bs4 import BeautifulSoup


# 1. 不使用cookie去请求大鹏的主页
dapeng_url = "http://www.renren.com/880151247/profile"
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
    "Cookie":"anonymid=jacdwz2x-8bjldx; depovince=GW; _r01_=1; _ga=GA1.2.1455063316.1511436360; _gid=GA1.2.862627163.1511436360; wp=1; JSESSIONID=abcrs0queAwRp_sk9dS-v; ch_id=10016; jebecookies=c68b9b55-b6a1-4661-8d11-832862cfa246|||||; ick_login=7e3299f4-1e31-4455-b2a4-e5317c9e2ccf; _de=EA5778F44555C091303554EBBEB4676C696BF75400CE19CC; p=a96969b7912d80d95127b7935c1b729e1; first_login_flag=1; ln_uact=970138074@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20170428/1700/main_nhiB_aebd0000854a1986.jpg; t=4d2ccb81ee83a6b1d3925b94779d22e21; societyguester=4d2ccb81ee83a6b1d3925b94779d22e21; id=443362311; xnsid=13bf03ea; loginfrom=syshome; jebe_key=9c062f5a-4335-4a91-bf7a-970f8b86a64e%7Ca022c303305d1b2ab6b5089643e4b5de%7C1511449232839%7C1; wp_fold=0"
}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)
with open('renren.html','w',encoding='utf-8') as fp:
    # write函数必须写入一个str的数据类型
    # resp.read()读出来的是一个bytes数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))