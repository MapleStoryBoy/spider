import numpy as np
from sklearn.preprocessing import StandardScaler, Imputer


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


if __name__ == '__main__':
    stand()
    im()
