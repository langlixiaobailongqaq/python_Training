#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_06_jd_lottery.py
@time: 2022/2/23  11:18
# @describe: 京东摇号小程序
"""

'''
需求:
1.允许用户最多选3次
2.每次放出20个车牌供用户选择
3.京[A-Z]-[xxxxx], 可以是数字和字母在组合
    想实现这个程序，有2个问题要解决:
        1.如何实现输出随机值
        2.随机值需限定在大写字母，和数字范围内，不能有其它特殊字符。
'''

# 京东摇号小程序-京Y-QL9Z6
import random, string

car_num_sample = string.digits+string.ascii_uppercase
print(random.sample(car_num_sample, 5))
count = 3
while count > 0:
    count -= 1
    print(count, '111111')
    num_list = []
    for i in range(20):
        second_letter = random.choice(string.ascii_uppercase)
        car_num = f'京{second_letter}-{"".join(random.sample(car_num_sample, 5))}'
        # car_num1 = ''.join(car_num.split())
        # num_list.append(car_num1)
        num_list.append(car_num)
        print(i, car_num)

    choice = input("输入你选择的号:").strip()
    if choice in num_list:
        exit(f'恭喜你选购成功，您的新车牌是{choice}')
    else:
        print(f'未选中，还有{count}次机会')


