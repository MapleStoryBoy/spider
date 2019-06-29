#encoding: utf-8

import csv

def read_csv_demo1():
    with open('stock.csv', 'r') as fp:
        # reader是一个迭代器
        reader = csv.reader(fp)
        next(reader)
        for x in reader:
            name = x[3]
            volumn = x[-1]
            print({'name': name, 'volumn': volumn})


def read_csv_demo2():
    with open('stock.csv','r') as fp:
        # 使用DictReader创建的reader对象
        # 不会包含标题那行的数据
        # reader是一个迭代器，遍历这个迭代器，返回来的是一个字典。
        reader = csv.DictReader(fp)
        for x in reader:
            value = {"name":x['secShortName'],'volumn':x['turnoverVol']}
            print(value)

if __name__ == '__main__':
    read_csv_demo2()
