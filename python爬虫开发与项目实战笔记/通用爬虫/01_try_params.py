import requests


headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
p = {"wd":"传智播客"}

url_temp = "https://www.baidu.com/s?"

r = requests.get(url_temp,headers=headers,params=p)

print(r.status_code)
print(r.request.url)