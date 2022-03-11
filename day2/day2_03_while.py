#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_03_while.py
@time: 2022/2/23  10:13
# @describe: while循环
"""

'''
# 3.1 死循环
count = 0
while True:
    # f, python3.6之后的语法
    print(f'第{count}次循环...')
    count += 1
'''

# 3.2 循环十次
count = 0
while count < 10:
    print(f'第{count}次循环...')
    count += 1


# 3.2 ⽤while 实现循环猜年龄
black_gf_age = 27
count = 0
while True:
    count += 1
    if count <= 3:
        guess = int(input('猜猜姑娘多大了...'))
        if guess > black_gf_age:
            print('猜的太大了，往小里猜...')
        elif guess < black_gf_age:
            print('猜的太小了，往大里猜...')
        else:
            exit('恭喜你，猜对了...')
    else:
        # strip 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
        choice = input("猜了3次还不对，真是笨呀，还玩么? [y/Y or n/N]").strip()
        #  不能写空值
        if len(choice) == 0 : choice
        if choice in ('y', 'Y'):
            count = 0
        elif choice in ('n', 'N'):
            exit('bye.')
        else:
            print('请输入正确的选项.')

