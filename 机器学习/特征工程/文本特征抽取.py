from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer


def countvec():
    '''
    文本数据特征抽取
    :return: None
    '''
    # 实例化
    cv = CountVectorizer()

    # 调用fit_transform
    # data = cv.fit_transform(['life is short,i like python', 'life is too long,i dislike python'])
    data = cv.fit_transform(["人生 苦短，我 喜欢 python", "人生漫长，不用 python"])
    print(cv.get_feature_names())  # 提取文渣中的单词，不重复，其实就相当于文章的特征
    # 对每篇文章，在词的列表里面进行统计每个词出现的次数，单个字母不统计

    print(data.toarray())  # toarray()方法将结果转换为数组形式
    return None


if __name__ == '__main__':
    countvec()
