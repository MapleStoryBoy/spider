#encoding: utf-8
import json

# json_str = '[{"username": "张三", "age": 18, "country": "china"}, {"username": "李赛", "age": 20, "country": "china"}]'
# persons = json.loads(json_str)
# print(type(persons))
# for person in persons:
#     print(person)

with open('person.json','r',encoding='utf-8') as fp:
    persons = json.load(fp)
    print(type(persons))
    for person in persons:
        print(person)