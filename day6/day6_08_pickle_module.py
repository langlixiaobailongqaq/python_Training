#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_08_pickle_module.py
@time: 2022/3/16  16:50
# @describe: pickle 模块
"""

"""
    pickle 模块四个功能：dumps、dump、loads、load

json vs pickle:
    JSON:
        优点：跨语⾔(不同语⾔间的数据传递可⽤json交接)、体积⼩
        缺点：只能⽀持int\str\list\tuple\dict
    Pickle:
        优点：专为python设计，⽀持python所有的数据类型
        缺点：只能在python中使⽤，存储数据占空间⼤

"""
import pickle


data = {'k1': 123, 'k2': 'Hello'}
# pickle.dumps 将数据通过特殊的形式转换位只有python语⾔认识的字符串
# dumps 会把数据变成bytes格式
p_str = pickle.dumps(data)
print(p_str)

# pickle.dump 将数据通过特殊的形式转换位只有python语⾔认识的字符串，并写⼊⽂件
with open('result.pk', 'wb') as fp:
    pickle.dump(data, fp)

# pickle.load 从文件里加载
f = open('result.pk', 'rb')
d = pickle.load(f)
print(d)