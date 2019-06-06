import numpy as np
from sklearn.preprocessing import StandardScaler, Imputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

def stand():
    '''
    标准化缩放
    :return:None
    '''
    std = StandardScaler()

    data = std.fit_transform([[1., -1., 3., ], [2., 4., 2.], [4., 6., -1., ]])

    print(data)

    return None


def im():
    """
    缺失值处理
    :return:NOne
    """
    # NaN, nan
    im = Imputer(missing_values='NaN', strategy='mean', axis=0) #axis=0是按列进行插补缺失值的

    data = im.fit_transform([[1, 2], [np.nan, 3], [7, 6]])

    print(data)

    return None

def var():
    """
    特征选择-删除低方差的特征
    :return: None
    """
    var = VarianceThreshold(threshold=1.0)

    data = var.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])

    print(data)
    return None


def pca():
    """
    主成分分析进行特征降维
    :return: None
    """
    pca = PCA(n_components=0.9)

    data = pca.fit_transform([[2,8,4,5],[6,3,0,8],[5,4,9,1]])

    print(data)

    return None


if __name__ == '__main__':
    stand()
    im()
    var()
    pca()
