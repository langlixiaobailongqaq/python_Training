#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_11_dict_del.py
@time: 2022/3/1  13:50
# @describe: dict 删除操作
"""
names = {
    'alex': [23, 'CEO', 66000],
    '葫芦娃': [24, '行政', 4000],
    '佩奇': [26, '讲师', 40000]
}

# 删除指定key
names.pop('alex')
print(names)

# 删除指定key，同pop 方法
del names['葫芦娃']
print(names)

# 清空dict
names.clear()
print(names)