#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_04_list_check.py
@time: 2022/3/1  10:48
# @describe: list 查操作
"""

names = ['⾦⻆⼤王', '⿊姑娘', 'rain', 'eva', '狗蛋', '银⻆⼤王', 'eva']
# 返回从左开始匹配到的第⼀个eva的索引
print(names.index('eva'))
# 返回eva的个数
print(names.count('eva'))
