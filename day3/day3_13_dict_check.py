#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_13_dict_check.py
@time: 2022/3/1  14:19
# @describe: dict 查操作
"""
names = {
    'alex': [30, '董事长', 999999],
    '葫芦娃': [24, '行政', 4000],
    '佩奇': [26, '讲师', 40000],
    '奥特曼': [18, '迪迦', 180]
}
# 返回字典中key对应的值，若key不存在字典中，则报错；
print(names['alex'])

# 返回字典中key对应的值，若key不存在字典中，则返回
names1 = names.get('qwdqwd', '不存在这个key')
print(names1)
# 存在则返回字典中key对应的值
print(names.get('奥特曼'))

# 若存在则返回True，没有则返回False
print('alex' in names)

# 返回⼀个包含字典所有KEY的列表
print(names.keys())

# 返回⼀个包含字典所有value 的列表
print(names.values())

# 返回⼀个包含所有（键，值）元组的列表
print(names.items())

# k, v 2个变量, 循环取出key，value值
for k, v in names.items():
    print(k, v)