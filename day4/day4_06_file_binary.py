#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_06_file_binary.py
@time: 2022/3/1  16:53
# @describe: 二进制：处理图片、视频文件
"""

"""
2进制模式打开⽂件:
    rb：2进制只读模式
    wb：2进制创建模式，若文件已存在，则覆盖旧文件
    ab：2进制追加模式，新数据会写到文件末尾
"""
gbk_file = ''
f = open('gbk_file', 'wb')
# 写⼊的⽂本要⽤字节类型
f.write('哈'.encode('gbk'))