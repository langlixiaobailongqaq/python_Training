#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_01_for.py
@time: 2022/2/23  09:41
# @describe: for循环/continue/break
"""

# for循环

for i in range(1, 10):
    print(i)

# 1.2 循环猜年龄
black_gf_age = 27
for i in range(3):
    guess = int(input("猜猜姑娘多大了？"))
    if guess > black_gf_age:
        print('猜的太大了，往小里试试...')
    elif guess < black_gf_age:
        print('猜的太小了，往大里试试...')
    else:
        exit('恭喜你，猜对了...')

# 1.3 打印50-100间奇偶数
for i in range(50, 100):
    if i % 2 == 1:
        print(i)


# 1.4 循环嵌套-⼀栋楼有5层，每层8间屋⼦，要求你把本楼所有的房间号打印⼀遍， 格式“1层-104”， “2层-205“
for i in range(1, 6):
    for j in range(1, 9):
        print(f'{i}层-{i}0{j}室')

# 1.5-continue:  遇到第3层时，不打印任何房间号，其它层都打印。
for i in range(1, 6):
    for j in range(1, 9):
        if i == 3:
            # 跳过本次循环，继续下次循环
            continue
        print(f'{i}层-{i}0{j}室')


# 1.6-break: 只结束当前这⼀层的循环
for i in range(1, 6):
    for j in range(1, 9):
        if i == 3:
            print('不走3层。。。')
            # 跳过本次循环，继续下次循环
            continue
        if i == 4 and j == 4:
            print('遇到鬼屋404了，不再继续了')
            # 结束当前循环， 注意只会结束第2层这个⼩循环。
            break
        print(f'{i}-{j}0{j}室')
