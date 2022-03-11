#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_02_triangle.py
@time: 2022/2/23  10:08
# @describe: 打印三角形
"""
n = 10
for i in range(n):
    if i < 5:
        print(i * '*')
    else:
        print((n-i) * '*')