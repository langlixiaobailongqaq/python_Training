#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_09_dict.py
@time: 2022/3/1  11:57
# @describe: dict
"""
# 语法 ｛key1:value1, key2:value2｝

info = {
    "name": "Alex Li",
    "age": 26
}


"""
特性：
    1. key-value 结构
    2. key 必须为不可变数据类型(字符串、数字)、必须唯一
    3、可存放任意多个value、可修改、可以不唯一
    4、无序，ordered_dict
    5、查询速度快，且不受dict 的大小影响
"""