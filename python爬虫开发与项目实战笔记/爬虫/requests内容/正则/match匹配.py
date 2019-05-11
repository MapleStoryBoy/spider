import re

content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
'''
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)

print(result.group())
print(result.span())
'''
'''
result = re.match('^Hello\s(\d+)\sWorld',content)
print(result)

print(result.group())
print(result.group(1))
print(result.span())
'''
'''
result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())
print(result.span())
'''
'''
group()方法输出了匹配的全部字符串，也就是说我们写的正则表达式匹配到了目标字
符串的全部内容; span()方法输州(o，的)，这是整个字符串的长度 。
'''
'''
#贪婪与非贪婪
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))
'''
'''
在贪婪匹配下， .*会匹配尽可能多的字符 。 正 则表达式中.*后面是\d+，
也就是至少一个数字，并没有指定具体多少个数字，因此， Y就尽可能匹配 
多的字符，这里就把 123456 匹配了，给\d+留下一个可满足条件的数字 7，
最后得到的内容就只有数 字7了。
'''

'''
#非贪婪匹配
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group(1))
'''
'''
content1 = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)',content1)
result2 = re.match('http.*?comment/(.*)',content1)
print('result1',result1.group(1))
print('result2',result2.group(1))
'''

#re.S修饰符的作用是使.匹配包括换行符在内的所有字符








