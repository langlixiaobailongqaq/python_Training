#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day2_07_annual_meeting_lottery.py
@time: 2022/2/23  14:29
# @describe: 年会抽奖程序
"""

'''
年会抽奖程序
    张三科技有限公司有300员⼯，开年会抽奖，奖项如下：
    ⼀等奖 3名， 泰国5⽇游
    ⼆等奖6名，Iphone⼿机
    三等奖30名，避孕套⼀盒
    规则：
    1. 共抽3次，第⼀次抽3等奖，第2次抽2等奖，第3次压轴抽1等奖
    2. 每个员⼯限中奖⼀次，不能重复
    
解题思路：
1. ⽣成⼀个员⼯列表，⽤random模块从⾥⾯取随机值
2. 取完值之后，⽴刻从员⼯⼤列表⾥把中奖⼈删掉，即可防⽌其再次中奖
'''
import random

staff_list = []
for i in range(1, 301):
    staff_list.append(i)
print(staff_list)

level = [30, 6, 3]
for i in range(3):
    winner_list = random.sample(staff_list, level[i])
    for w in winner_list:
        staff_list.remove(w)
    print(f'抽中{3-i}等奖的人是:', winner_list)




