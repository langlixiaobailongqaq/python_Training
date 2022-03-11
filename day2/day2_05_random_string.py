#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_05_random_string.py
@time: 2022/2/23  14:34
# @describe: random/string
"""

# 5.1 random 模块-可以产生知道范围内的随机数、字符串等
import random

ran = random.choice('abcdefghi')
ran1 = random.choice(['a', 'f', 'v', 'b', 't', 'h', 'j'])
s = 'qwsedcvfrtgnhjk'
# 从数据源s中随机取出3个值
ran2 = random.sample(s, 3)
# 打印一个随机数
ran3 = random.randint(1, 100)
print(ran, ran1, ran2, ran3)


# 5.2 string 模块-关于字符串的处理函数
import string

# 小写加大写字母
str_a_A = string.ascii_letters
# 大写字母
str_A = string.ascii_uppercase
# 小写字母
str_a = string.ascii_lowercase
# 特殊字符
str_ts = string.punctuation
# 数字
str_number = string.digits
print(str_a_A, '\n',  str_A, '\n', str_a, '\n', str_ts, '\n', str_number)
