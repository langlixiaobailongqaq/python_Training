#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_01_file.py
@time: 2022/3/1  16:10
# @describe: 文件操作
"""
"""
文件打开模式：
    r 只读模式；
    w 创建模式，若文件已存在，则覆盖旧文件；
    a 追加模式，新数据会写到文件末尾
"""

filename = ''
# 打开文件
f = open(filename)
# 写操作
f.write()
# 读操作
f.read()
# 保存并关闭
f.close()