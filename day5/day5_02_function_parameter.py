#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_02_function_parameter.py
@time: 2022/3/12  12:23
# @describe: 函数的各种参数
"""

"""
形参变量：
    只有在被调用时才分配内存单元，在调用结束时，即刻释放所分配的内存单元。因此，形参只有在函数内部有效。
    函数调用结束返回主调用程序代码后则不能再使用该形参变量
    
实参：
    可以是变量、任意数据类型、表达式、函数等，无论实参是何种类型的变量，在进行函数调用时，
    它们都必须有确定的值，以便把这些值传送给形参。因此应预先给实参赋值。
    
默认参数：
    默认参数是在定义时赋值，且仅仅赋值一次。
    解释器在处理函数参数时，按优先级，位置参数>默认参数
    
关键参数(指定参数)：
    正常情况下，给函数传参数要按顺序，不想按顺序就可以用关键参数，只需指定参数名即可（指定了参数名的参数就叫关键参数），
    但记住一个要求：关键字参数必须放在位置参数（以位置顺序确定对应关系的参数）之后。
        解释器在处理函数参数时，按优先级，位置参数>关键参数

非固定参数：
    若你的函数在定义时不确定用户想传入多少个参数，就可以使用非固定参数

"""


# 形参-x, y
def calc(x, y):
    res = x ** y
    return res


# 实参-a, b
a = b = 2
c = calc(a, b)
print(c)


# 默认参数
def stu_register(name, age,  course, country='CN'):
    print("--- 注册学生信息 ---")
    print("姓名:", name)
    print("年龄:", age)
    print("课程:", course)
    print("国籍:", country)


stu_register('Mack', 22, 'java')
stu_register('Mack', 22, 'Python', 'US')


# 关键参数(指定参数)
stu_register('王大鹏', course='Py', age=22, country='CN')


# 非固定参数- *args 会把多传入的参数变成一个元组形式
def stu_register(name, age, *args):
    print(name, age, args)


# 后面的（）就是args， args没传值，所以为空
stu_register('Alex', 22)
stu_register('jack', 18, 'CN', 'Py')


# 非固定参数- *kwargs 会把多传入的参数变成一个dict 形式
def stu_register(name, age, *args, **kwargs):
    print(name, age, args, kwargs)


# Alex 2 () {} ,{}就是kwargs，没传值，所以为空
stu_register('Alex', 2)
stu_register('Alex', 20, 'CN', 'Py', sex='Male', province='ShangHai')