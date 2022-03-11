#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_12_dict_update.py
@time: 2022/3/1  13:55
# @describe: dict 修改操作
"""

names = {
    'alex': [23, 'CEO', 66000],
    '葫芦娃': [24, '行政', 4000],
    '佩奇': [26, '讲师', 40000]
}

# 如果key 在字典中存在，'new_value'将会替代原来的value值
# 语法：dic['key] = 'new_value'
names['alex'] = [30, '董事长', 999999]
print(names)
names['奥特曼'] = [18, '迪迦', 180]
print(names)