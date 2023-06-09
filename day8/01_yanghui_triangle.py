#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: 01_yanghui_triangle.py
@time: 2023/2/16  09:28
# @describe: 杨辉三角形
它的一个重要性质是：三角形中的每个数字等于它两肩上的数字相加。
    下面给出了杨辉三角形的前4行：
    1
    1 1
    1 2 1
    1 3 3 1

给出n，输出它的前n行。

输入格式
输入包含一个数n。

输出格式：
    输出杨辉三角形的前n行。每一行从这一行的第一个数开始依次输出，中间使用一个空格分隔。请不要在前面输出多余的空格。
    样例输入：
    4
    样例输出：
    1
    1 1
    1 2 1
    1 3 3 1
"""

# 用户输入数字
value = int(input("请输入数字："))
# 记录 index-1 行的数字
index = 0
data = []
while index < value:
    # 记录 index 行的数字(当前行)
    data1 = []
    for i in range(0, (len(data)+1)):
        if int(i) == 0:
            data1.append(1)
            # 不换行输出
            print(str(1) + " ", end="")
        if int(i) < (len(data) - 1):
            data1.append(data[i] + data[i+1])
            print(str(data[i] + data[i+1]) + " ", end="")
        if int(i) > 0 and int(i) == len(data):
            data1.append(1)
            # 不换行输出
            print(str(1) + " ", end="")

    # 行数加1
    index = int(index) + 1
    # 当前行输出完毕，将当前行的数字赋值给上一行
    data = data1
    # 换行
    print('\n')

