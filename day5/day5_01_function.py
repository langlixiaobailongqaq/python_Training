#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_01_function.py
@time: 2022/3/11  20:15
# @describe: 函数
"""

"""
    函数定义：函数是指将一组语句的集合通过一个名字(函数名)封装起来，要想执行这个函数，
            只需调用其函数名即可。
    特性：
        1、减少重复代码
        2、使程序变的可扩展
        3、使程序变得易维护
"""


# 语法定义
def sayhi():    # 函数名
    print('hello')

# 调用函数
sayhi()


# 带参数
def calc(x, y):
    res = x ** y
    # 函数执行结果
    print(res)


calc(5, 22)