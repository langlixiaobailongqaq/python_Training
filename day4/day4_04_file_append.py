#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_04_file_append.py
@time: 2022/3/1  16:32
# @describe: 追加模式
"""
f = open(file='联系⽅式.txt', mode='a')
f.write('8. 黑姑娘 北京 168 48 12345678911\n')
f.close()