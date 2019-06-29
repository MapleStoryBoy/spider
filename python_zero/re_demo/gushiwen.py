#encoding: utf-8

import re
import requests

url = "http://www.gushiwen.org/default_1.aspx"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
response = requests.get(url,headers=headers)
text = response.text

titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>',text,re.S)
dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.S)
authors = re.findall(r'<p\sclass="source">.*?<a.*?<a.*?>(.*?)</a>',text,re.S)
poem_tags = re.findall(r'<div class="contson".*?>(.*?)</div>',text,re.S)
poems = []
for poem_tag in poem_tags:
    poem = re.sub(r'<.*?>',"",poem_tag)
    poems.append(poem.strip())

poem_infos = zip(titles,dynasties,authors,poems)

poem_list = []
for poem_info in poem_infos:
    title,dynasty,author,poem = poem_info
    poem_list.append({"title":title,"dynasty":dynasty,"author":author,"poem":poem})

for x in poem_list:
    print(x)