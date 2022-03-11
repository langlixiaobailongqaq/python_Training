#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day_01_demo.py
@time: 2022/2/24  09:49
# @describe: 课后练习
"""

'''
11.2 写个匹配成绩的⼩程序，成绩有ABCDE 5个等级，与分数的对应关系如下
    A 90-100
    B 80-89
    C 60-79
    D 40-59
    E 0-39
要求⽤户输⼊0-100的数字后，你能正确打印他的对应成绩等级，⽐如输⼊的是75，则打印C
'''


try:
    fraction = int(input("请输入您的成绩："))
    if fraction >= 90 and fraction <= 100:
        print('您的成绩是：A')
    elif fraction >= 80 and fraction <= 89:
        print('您的成绩是：B')
    elif fraction >= 60 and fraction <= 79:
        print('您的成绩是：C')
    elif fraction >= 40 and fraction <= 59:
        print('您的成绩是：D')
    elif fraction >= 0 and fraction <= 39:
        print('您的成绩是：E')
except:
    print('请输入整数')
