# coding=utf-8
import requests

#发送请求
response =  requests.get("https://www.baidu.com/img/bd_logo1.png")

#保存
with open("a.png","wb") as f:
    f.write(response.content)