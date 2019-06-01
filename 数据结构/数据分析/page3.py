from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y1,label="自己",color="orange",linestyle=':',linewidth=1)
plt.plot(x,y2,label="同桌",color="cyan",linestyle='-.',linewidth=1)
#设置x轴刻度
_xtick_lables = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_lables,fontproperties=my_font)
plt.yticks(range(9))

#绘制网格，alpha指定网格的显示透明度
plt.grid(alpha=0.1,linestyle=':')

#添加图列和中文显示
plt.legend(prop=my_font)


plt.show()