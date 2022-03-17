#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_07_json_module.py
@time: 2022/3/16  16:29
# @describe: 序列化json模块
"""

"""
JSON(JavaScriptObject Notation, JS 对象简谱) ：
    是⼀种轻量级的数据交换格式。它采⽤完全独⽴于编程语⾔的⽂本格式来存储和表示数据。
    简洁和清晰的层次结构使得 JSON 成为理想的数据交换语⾔。 易于
    ⼈阅读和编写，同时也易于机器解析和⽣成，并有效地提升⽹络传输效率。
    
Json的作⽤：⽤于不同语⾔接⼝间的数据交换。可以帮各个语⾔之间实现数据类型的相互转换。

四个功能：dumps、dump、loads、load

JSON⽀持的数据类型：
    Python中的字符串、数字、列表、字典、集合、布尔 类型，都可以被序列化成JSON字符串，被其它任何编程语⾔解析。
    
什么是序列化？
    序列化是指把内存⾥的数据类型转变成字符串，以使其能存储到硬盘或通过⽹络传输到远程，因为硬盘
    或⽹络传输时只能接受bytes。
    
为什么要序列化？
    你打游戏过程中，打累了，停下来，关掉游戏、想过2天再玩，2天之后，游戏⼜从你上次停⽌的地⽅继
    续运⾏，你上次游戏的进度肯定保存在硬盘上了，是以何种形式呢？游戏过程中产⽣的很多临时数据是
    不规律的，可能在你关掉游戏时正好有10个列表，3个嵌套字典的数据集合在内存⾥，需要存下来？你
    如何存？把列表变成⽂件⾥的多⾏多列形式？那嵌套字典呢？根本没法存。所以，若是有种办法可以直
    接把内存数据存到硬盘上，下次程序再启动，再从硬盘上读回来，还是原来的格式的话，那是极好的。
"""
import json


name = ['葫芦娃', 'Al', '我是大哥大']
# json 序列化，将数据通过特殊的形式转换位所有程序语⾔都认识的字符串
names = json.dumps(name)

# json 反序列化
print(names, '\n', json.loads(names))

# dump 将数据保存在 json文件中
data = {"name": "cc", "age": 10}
with open('result.json', 'w') as fp:
    json.dump(data, fp)

# load-从json文件中读取数据，变成python
with open('result.json') as f:
    d = json.load(f)
    print(d)