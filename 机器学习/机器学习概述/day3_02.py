from sklearn.datasets import fetch_20newsgroups,load_boston

#news = fetch_20newsgroups(subset='all')

#print(news.data)
#print(news.target)
lb = load_boston()

print("获取特征值")
print(lb.data)
print("目标值")
print(lb.target)
print(lb.DESCR)








