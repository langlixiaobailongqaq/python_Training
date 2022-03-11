#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_02_file_write.py
@time: 2022/3/1  16:17
# @describe: 创建文件
"""
# 若文件已存在，则覆盖
f = open(file='/Users/zhengxin/PycharmProjects/pythonProject1/day4/staff.txt', mode='w')
f.write('Alex CEO 600\n')
f.write('葫芦娃 行政 5000\n')
f.close()