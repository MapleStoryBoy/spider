from urllib.parse import parse_qs,parse_qsl

query = 'name=jsp&age=23'
print(parse_qs(query))


print(parse_qsl(query))