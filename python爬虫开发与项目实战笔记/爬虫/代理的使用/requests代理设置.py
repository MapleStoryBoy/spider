import requests

proxy = '123.169.37.151'
proxies = {
    'http':'http://' + proxy,
    'https':'https://' + proxy
}

try:
    response = requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error',e.args)


