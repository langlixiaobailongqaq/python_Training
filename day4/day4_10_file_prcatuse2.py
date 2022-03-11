#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_10_file_prcatuse2.py
@time: 2022/3/11  11:37
# @describe: 练习
 三、综合实战-股票数据分析&处理：
    把以下股票数据存⼊stock_data.txt
    开发程序对 stock_data.txt 进⾏以下操作：
    1. 程序启动后，给⽤户提供查询接⼝，允许⽤户᯿复查股票⾏情信息(⽤到循环)
    2. 允许⽤户通过模糊查询股票名，⽐如输⼊“啤酒”, 就把所有股票名称中包含“啤酒”的信息打印出来
    3. 允许按股票价格、涨跌幅、换⼿率这⼏列来筛选信息，⽐如输⼊“价格>50”则把价格⼤于50的股票
都打印，输⼊“市盈率(TTM)<50“，则把市盈率⼩于50的股票都打印，不⽤判断等于。
    思路提示：加载⽂件内容到内存，转成dict or list结构，然后对dict or list 进⾏查询等操作。 这样以后
就不⽤每查⼀次就要打开⼀次⽂件了，效率会⾼。

"""
list_data = []
# 用来判断该列字符串最后一位是不是数字
q_list = [4, 5, 6, 7, 8, 10]
# 用来处理两列单位不一致的
d_list = [7, 11]
# 将数据转化成一个列表
with open('stock_data.txt', 'r', encoding='utf-8') as f:
    # 股票参数名列表
    list_name = f.readline().strip('\n').split(',')
    for line in f:
        line = line.strip('\n')
        list_data.append(line.split(','))

while True:
    s = input('股票查询接口>>').strip()
    print(list_name)
    if '>' in s:
        # 命令分隔
        index = s.index('>')
        name = s[0: index]
        date = s[index+1:]
        # 获取所查的列数
        l_index = list_name.index(name)
        # 处理列有百分号的情况
        if l_index in q_list:
            for l in list_data:
                try:
                    if float(l[l_index][0:-1]) > float(date):
                        print(l)
                except ValueError as e:
                    continue
        # 处理两列单位不同的情况
        elif l_index in d_list:
            for l in list_data:
                if '亿' in l[l_index]:
                    if float(l[l_index][0:-1]) * 10000 > float(date):
                        print(l)
                if float(l[l_index][0:-1]) > float(date):
                    print(l)
        else:
            for l in list_data:
                try:
                    if float(l[l_index]) > float(date):
                        print(l)
                except ValueError as e:
                    continue
    # 处理小于的情况
    elif '<' in s:
        index = s.index('<')
        name = s[0:index]
        date = s[index + 1:]
        # 获取所查的列数
        l_index = list_name.index(name)
        # 处理列有百分号的情况
        if l_index in q_list:
            for l in list_data:
                try:
                    if float(l[l_index][0:-1]) < float(date):
                        print(l)
                except ValueError as e:
                    continue
        # 处理两列单位不同的情况
        elif l_index in d_list:
            for l in list_data:
                if '亿' in l[l_index]:
                    if float(l[l_index][0:-1]) * 10000 < float(date):
                        print(l)
        else:
            for l in list_data:
                try:
                    if float(l[l_index]) < float(date):
                        print(l)
                except ValueError as e:
                    print(l)
    else:
        for l in list_data:
            if s in l[1]:
                print(l)
