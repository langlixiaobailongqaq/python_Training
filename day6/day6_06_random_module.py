#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_06_random_module.py
@time: 2022/3/16  16:10
# @describe: random随机数 模块
"""
import random


# 返回1-10 之间的一个随机数，不包括10
random_number = random.randrange(1, 10)
print(random_number)

# 返回1-10之间的随机数，包括10
random.randint()

# 随机选取0到100间的偶数
random.randrange(0, 100, 2)

# 返回一个随机浮点数
random.random()

# 返回一个给定数据集中的随机字符
random.choice('abce3#$@1')

# 从多个字符中选取特定数量的字符
random.sample('abcdefghij', 3)

# 生成随机字符串
import string
''.join(random.sample(string.ascii_lowercase + string.digits, 6))

# 洗牌
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(a)

