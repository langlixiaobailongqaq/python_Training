#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_05_list_slice.py
@time: 2022/3/1  10:55
# @describe: 列表切片
"""
# 语法 names[start : end], 特性：顾头不顾尾
names = ['⾦⻆⼤王', '⿊姑娘', 'rain', 'eva', '狗蛋', '银⻆⼤王', 'eva']

# 不包含下标4 的元素
print(names[1:4], names[0:4], names[:4])

# 取倒数后2 个值
print(names[5:])

# 倒着切
print(names[-5:-1], names[-5:])

# 跳着切(步长): names[start:end:step] , step 默认是1
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 设置步长为2
print(a[0:7:2])
# 按步⻓3打印列表，第1个:是省略掉的start:end
print(a[::3])