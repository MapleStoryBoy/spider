#encoding: utf-8

import json

# 将python对象转换为json字符串

persons = [
    {
        'username':"张三",
        'age': 18,
        'country': 'china'
    },
    {
        'username': '李赛',
        'age': 20,
        'country': 'china'
    }
]


# json_str = json.dumps(persons)
# with open('person.json','w',encoding='utf-8') as fp:
#     # fp.write(json_str)
#     json.dump(persons,fp,ensure_ascii=False)

class Person(object):
    country = 'china'

a = {
    'person': Person()
}
json.dumps(a)
