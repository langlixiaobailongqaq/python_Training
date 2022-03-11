#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_14_dict_for.py
@time: 2022/3/1  14:41
# @describe: dict 循环
"""
names = {
    'alex': [30, '董事长', 999999],
    '葫芦娃': [24, '行政', 4000],
    '佩奇': [26, '讲师', 40000],
    '奥特曼': [18, '迪迦', 180]
}
# 循环取出k 值
for k in names.keys():
    print(k)

# 循环取出k，v 值
for k, v in names.items():
    print(k, v)

# 推荐⽤这种，效率速度最快
for k in names:
    print(k)

info = {
    "name": "路⻜学城",
    "mission": "帮⼀千万极客⾼效学编程",
    "website": "https://luffycity.com"
}
for k in info:
    print(k, info[k])

# 求长度 len()⽅法可同时⽤于列表、字符串
print(len(info))