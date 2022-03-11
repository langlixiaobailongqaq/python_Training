#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_05_file_for.py
@time: 2022/3/1  16:40
# @describe: 文件for
"""
f = open(file='联系⽅式.txt', mode='r')
for line in f:
    line = line.split()
    number, name, addr, height, weight, phone = line
    height = int(height)
    weight = int(weight)
    # 只打印身⾼>170 and 体᯿<=50的
    if height > 170 and weight <= 50:
        print(line)
f.close()