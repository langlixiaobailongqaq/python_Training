#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_04_99multiplication_table.py
@time: 2022/2/23  11:02
# @describe: 99乘法表
"""

for i in range(1, 10):
    for j in range(1, i+1):
        print(f'{i}x{j}={i*j}', end=' ')
    # 打印空行
    print()