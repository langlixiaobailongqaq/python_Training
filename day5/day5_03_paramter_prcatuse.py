#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_03_paramter_prcatuse.py
@time: 2022/3/12  13:21
# @describe: 函数参数练习
"""

"""
    根据下图所示，对 print_info 里的代码进行实现
    def print_info(*args, **kwargs): ...
    
    print_info(name='Alex', gae=22, sex='M')
    print_info(name='Jack', gae=26, sex='M', hobbie='学习')
    
    
--- info ---
Name: Alex
Age: 22
Sex: M
Hobbie: 大保健
--- info ---
Name: Jack
Age: 26
Sex: M
Hobbie: 学习

"""


def print_info(*args, **kwargs):
    count = 1
    for k, v in kwargs.items():
        if 'hobbie' in k:
            if count == 1:
                print('--- info ---')
                print('Name:' + kwargs['name'])
                print('Age:' + str(kwargs['age']))
                print('Sex:' + kwargs['sex'])
                kwargs['hobbie'] = '大保健'
                print('Hobbie:' + kwargs['hobbie'])
                count += 1
                print('--- info ---')
            if count == 2:
                print('Name:' + kwargs['name'])
                print('Age:' + str(kwargs['age']))
                print('Sex:' + kwargs['sex'])
                kwargs['hobbie'] = '学习'
                print('Hobbie: ' + kwargs['hobbie'])


print_info(name='Alex', age=22, sex='M')
print_info(name='Jack', age=26, sex='M', hobbie='学习')