#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_07_fried_gold.py
@time: 2022/3/14  14:11
# @describe: 练习题-炸金花棋牌游戏

需求：
    1. 允许⽤户⼀次性输⼊多个玩家姓名，不限个数，然后为每个玩家随机⽣成3张牌
    2. 你只有⼀付扑克牌，确保发出去的每张牌不重样
    3. 牌需要有⿊桃、红桃、⽅⽚、梅花之分

"""

import random


def create_poke():
    nums = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    card_types = ['红桃', '黑桃', '方片', '梅花']
    full_poke_cards = []
    for i in card_types:
        for n in nums:
            full_poke_cards.append([i, n])
    print(full_poke_cards)
    return full_poke_cards


def issue_cars(*args):
    """
    发牌
    :param args: 玩家姓名列表
    :return:
    """
    card_list = create_poke()
    #  random.shuffle:将序列的所有元素随机排序(洗牌)
    random.shuffle(card_list)
    print(card_list)
    # fromkeys 函数用于创建一个新字典，以序列 seq 中元素做字典的键，value 为字典所有键对应的初始值。
    players = {}.fromkeys(args, [])
    for p in players:
        # samole: 从序列seq中选择n个随机且独立的元素
        random_cards = random.sample(card_list, 3)
        print(random_cards)
        # 给玩家发牌
        players[p] = random_cards
        # 删掉已发了的牌
        for i in random_cards:
            card_list.remove(i)

    return players


player_cars = issue_cars('Alex', 'Jack')
print(player_cars)