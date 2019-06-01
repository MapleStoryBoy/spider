from matplotlib import pyplot as plt


x = range(2,26,2)
y = [15,13,14,5,17,20,25,26,27,22,18,15]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)
'''
figure图形图标的意思，在这里指的就是我们画的图
通过实例化figure并且传递参数，能够在后台自动使用该figure实例
在图像模糊的时候传入dpi参数，让图片更加清晰
'''




#绘图
plt.plot(x,y)

#设置x轴的刻度
_xtick_lables = [i/2 for i in range(4,49)]
plt.xticks(_xtick_lables[::3])
#保存图片
plt.savefig("./t1.png")#可以保存svg格式，在网页中打开可以不失真
#展示
plt.show()