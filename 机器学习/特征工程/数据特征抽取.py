# 特征抽取

from sklearn.feature_extraction.text import CountVectorizer

# 实例化CountVectorizer
vector = CountVectorizer()

# 调用fit_transform输入并转换数据
res = vector.fit_transform(['life is short,i like python', 'life is too long,i dislike python'])

# 打印结果
print(vector.get_feature_names())
print(res.toarray())


