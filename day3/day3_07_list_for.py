#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_07_list_for.py
@time: 2022/3/1  11:24
# @describe: 循环列表
"""
names = ['#', '4', '@', 'eva', 'rain', '狗蛋', '⾦⻆⼤王', '银⻆⼤王', '⿊姑娘']
for i in names:
    print(i)

# 打印索引
for i in enumerate(names):
    print(i[0], i[1])
