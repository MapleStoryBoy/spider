import requests


headers = {
    'Cookie':'tgw_l7_route=7bacb9af7224ed68945ce419f4dea76d; _zap=6b936ea0-ef53-4d90-b684-ce541248a20b; _xsrf=6BGECft0hGjVHiEhdHyXS7ROUa8Ht327; d_c0="ABBpkjePaQ-PTvePaMiQYy_LDLLB2ddwrOw=|1557562011"; capsion_ticket="2|1:0|10:1557562022|14:capsion_ticket|44:OTM3ZDAzYTJlMTRiNGFjNWI3NDkwZDAzNTc2MzM1M2Y=|10d21ca0b7d2e97a246369cfbc1dcb66dca8a84eeb1fea881b7f3f09baabc4d1"; z_c0="2|1:0|10:1557562063|4:z_c0|92:Mi4xT3h1c0R3QUFBQUFBRUdtU040OXBEeVlBQUFCZ0FsVk56OUREWFFEXzE2VXNyeU1tcEhKblc2VklOTG9Da19uOE1R|48a52e0ff2790bce7bba14b36e8b9e05544665c02ddeb703031550fef4bbbb8a"; tst=r; q_c1=9a9eddc8a23a45bdb65037783ba2a56e|1557562068000|1557562068000; __gads=ID=708eccfd22e9c60c:T=1557562120:S=ALNI_MaKZXT40oN-JAjJXXUkp-aPWK4a1g',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/4.0 (compatible; MSIE S.S; Windows NT)'
}

r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)