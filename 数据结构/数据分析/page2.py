from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

#matplotlib.rc  windows和linux
'''
font = {'family': 'monospace',
        'weight': 'bold',
        'size': 'larger'}
matplotlib.rc("font",**font)
'''
#另外一种设置字体的方式
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y)

#调整x轴的刻度
_x = list(x)
_xtick_lables = ['10点{}分'.format(i) for i in range(60)]
_xtick_lables += ['11点{}分'.format(i) for i in range(60)]


#取步长
plt.xticks(_x[::3],_xtick_lables[::3],rotation=45,fontproperties=my_font)#rotation旋转角度


#添加x，y轴描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(°C)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)

plt.show()