#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_01_list_add.py
@time: 2022/2/24  10:09
# @describe: 列表添加: append、insert、extend
"""

# 追加，数据会追到尾部
names = ['alex', 'jack']
names.append('rain')
print(names)

# 插⼊，可插⼊任何位置
names.insert(2, '葫芦娃')
print(names)

# 合并，可以把另一列表的值合并进来
n2 = ["狗蛋", "绿⽑", "鸡头"]
names = ['alex', 'jack', '⿊姑娘', 'rain', 'eva']
names.extend(n2)
print(names)

# 列表嵌套
names.insert(2, [1, 2, 3])
print(names, names[2][1])
