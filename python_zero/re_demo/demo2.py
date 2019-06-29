#encoding: utf-8
import re

# text = "apple price is $299"
# ret = re.search("\$\d+",text)
# print(ret.group())

# r = raw = 原生的
# text = '\n'
# print(text)

text = "\c" #= '\n'
# python：'\\n' = \n
# \\\\n =》 \\n
# \\c

# 正则表达式中：\n =
# \\n =》 \n
# \\c =》 \c
ret = re.match(r'\\c',text)
print(ret.group())