#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day3_15_dict_practise.py
@time: 2022/3/1  14:53
# @describe: dict 练习题
"""

# 1. ⽣成⼀个包含100个key的字典，每个value的值不能⼀样
key = {}
for i in range(100):
    key.setdefault(i, f"我是{i}")
print(key)

# 2.请把下面dict中key⼤于5的 值value打印出来。
dic = {
    'k0': 0,
    'k1': 1,
    'k2': 2,
    'k3': 3,
    'k4': 4,
    'k5': 5,
    'k6': 6,
    'k7': 7,
    'k8': 8,
    'k9': 9
    }
for v in dic.values():
    if v > 5:
        print(v)

# 把题2中value是偶数的统⼀改成-1
for v in dic.values():
    if v % 2 == 0:
        v = -1
    print(v)

# 4.请设计⼀个dict, 存储你们公司每个⼈的信息， 信息包含⾄少姓名、年龄、电话、职位、⼯资，并
# 提供⼀个简单的查找接⼝，⽤户按你的要求输⼊要查找的⼈，你的程序把查到的信息打印出来
names = {
    "小明": [18, 199, "销售", 8000],
    "小白": [20, 110, "安全", 9000]
}
user_input = input("请输入你要查找人的名字：")
for k in names:
    count = 0
    if k == user_input:
        print(f"{k}的年龄是{names[k][0]},电话是{names[k][1]},职业是{names[k][2]}, 工资是{names[k][3]}")
    else:
        print('查无此人')