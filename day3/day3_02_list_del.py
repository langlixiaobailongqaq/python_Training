#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_02_list_del.py
@time: 2022/3/1  09:50
# @describe: 列表删除操作-del、pop、remove、clear
"""
# del 直接删除
names = ['alex', 'jack', [1, 2, 3], '⿊姑娘', 'rain', 'eva', '狗蛋', '绿⽑', '鸡头']
del names[2]
print(names)

# pop删除
names = ['alex', 'jack', '⿊姑娘', 'rain', 'eva', '狗蛋', '绿⽑', '鸡头']
# 默认删除最后⼀个元素并返回被删除的值
print(names.pop(), names)
names = ['alex', 'jack', '⿊姑娘', 'rain', 'eva', '狗蛋', '绿⽑']
# help(names.pop)
# 删除指定元素
print(names.pop(1))

# remove 删除
names = ['alex', 'jack', '⿊姑娘', 'rain', 'eva', '狗蛋', '绿⽑', '鸡头', 'eva']
# 删除第⼀个找到的eva值
names.remove('eva')
print(names)

# clear 清空
n2 = ['狗蛋', '绿⽑', '鸡头']
n2.clear()
print(n2)