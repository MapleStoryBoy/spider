#encoding: utf-8

import re

# 分组
# text = "apple's price $99,orange's price is $10"
# ret = re.search('.*(\$\d+).*(\$\d+)',text)
# print(ret.group(0))
# ret.group(0) = ret.group()
# print(ret.group(1))
# print(ret.group(2))
# print(ret.group(1,2))
# 所有的子分组都拿出来
# print(ret.groups())

# find_all函数：
# text = "apple's price $99,orange's price is $10"
# ret = re.findall('\$\d+',text)
# print(ret)

# sub函数：
# text = "apple's price $99,orange's price is $10"
# ret = re.sub('\$\d+',"0",text)
# print(ret)

# html = """
# <dd class="job_bt">
#         <h3 class="description">职位描述：</h3>
#         <div>
#         <p>参与公司新一代面向生命科学行业云服务应用及平台的开发。</p>
# <p><br></p>
# <p>【工作职责】</p>
# <p>云服务软件产品的架构设计与开发</p>
# <p>与设计、产品及前端人员沟通，保证产品的质量和开发进度</p>
# <p>研究新兴技术，对产品进行持续优化</p>
# <p><br></p>
# <p>【职位要求】</p>
# <p>计算机相关专业本科及以上学历</p>
# <p>对常见数据结构和面向对象设计有深入理解</p>
# <p>熟练掌握Python语言，3年以上实际经验</p>
# <p>熟悉Python Web开发框架如Django</p>
# <p>熟练掌握数据库开发和设计</p>
# <p>基本的英文读写能力</p>
#
#         </div>
#     </dd>
# """
# ret = re.sub('<.+?>',"",html)
# print(ret)

# split函数：
# text = "hello&world ni hao"
# ret = re.split('[^a-zA-Z]',text)
# print(ret)

text = "the number is 20.50"
# r = re.compile('\d+\.?\d*')
r = re.compile(r"""
    \d+ # 小数点前面的数字
    \.? # 小数点本身
    \d* # 小数点后面的数字
""",re.VERBOSE)
ret = re.search(r,text)
print(ret.group())