#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_03_file_read.py
@time: 2022/3/1  16:23
# @describe: 只读模式
"""
f = open(file='联系⽅式.txt', mode='r')
# 读一行
print(f.readline())
print('------分隔符-------')
# 读所有，剩下的所有
data = f.read()
print(data)
f.close()
