#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_05_local_global_variable.py
@time: 2022/3/13  13:33
# @describe: 局部/全局变量

    在函数中定义的变量成为局部变量，在程序的一开始定义的变量称为全局变量。
    全局变量作用域(即有效范围)是整个程序，局部变量作用域是定义该变量的函数。
    变量的查找顺序是 局部变量>全局变量。
    当全局变量与局部变量同名时，在定义局部变量的函数内，局部变量起作用；在其它地方，全局变量起作用。
    在函数里不能直接修改全局变量。
"""

name = 'Alex'

def change_name():
    name = '金角大王'
    print('after changr', name)


change_name()
print(name)


# 在函数里修改全局变量
name = 'Alex'

def change_name():
    # 声明一个全局变量
    global name
    name = '金角大王001'
    print('after changr', name)


change_name()
print(name)