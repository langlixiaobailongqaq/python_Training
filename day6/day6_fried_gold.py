#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_fried_gold.py
@time: 2022/3/14  15:25
# @describe: 炸金花

游戏规则：
    一付扑克牌,去掉大小王，每个玩家发3张牌,最后比大小，看谁赢。
    有以下几种牌:
        豹子:三张一样的牌，如3张6.
        顺金:又称同花顺，即3张同样花色的顺子，如红桃5、6、 7
        顺子:又称拖拉机，花色不同，顺子，如红桃5、方片6、黑桃7,组成的顺子
        对子: 2张牌- -样.
        单张:单张最大的是A
        这几种牌的大小顺序为，豹子>顺金>同花>顺子>对子>单张

    思路：不同等级(牌型)加不同权重值
    高内聚低耦合
"""


# 1.生成牌
import random


def generate_pokes():
    poke_types = ['♥', '♠', '♣', '♦']
    poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    poke_list = []
    # 循环花色
    for p_type in poke_types:
        # 将牌的值定义出来，后面的值方便计算
        count = 2
        # 循环点数
        for p_num in poke_nums:
            card = [f"{p_type}{p_num}", count]
            count += 1
            poke_list.append(card)
    print(poke_list)
    return poke_list


poke_list = generate_pokes()


players = ['德玛西亚', '疾风剑豪', '剑圣', '德邦', '皇子', '妖姬', '加里奥']

# 2.发牌
def issue_cards(players, poke_list):
    # 保存发牌结果，用字典存对应玩家的牌
    player_dic = {}
    for p_name in players:
        # 随机取出三张牌
        p_cards = random.sample(poke_list, 3)
        # 每发完一个人的牌，剔除
        for card in p_cards:
            poke_list.remove(card)
        player_dic[p_name] = p_cards
        print(f"为玩家{p_name}生成了牌", p_cards)
    return player_dic


player_dic = issue_cards(players, poke_list)


""" 3.写好每种牌型的判断规则函数 """
# 排序
def sort_list(lis):
    l = len(lis)
    # 冒泡排序
    for i in range(0, l):
        for j in range(0, l-i-1):
            if lis[j][1] > lis[j+1][1]:
                lis[j], lis[j+1] = lis[j+1], lis[j]
    return lis

# 单牌
def calculate_Single(p_cards, score):
    score = 0
    p_cards = sort_list(p_cards)
    weight_val = [0.1, 1, 10]
    count = 0
    # 三张牌按照设定的比重从小到大相乘，结果相加得到最后的分数
    for card in p_cards:
        score += card[1] * weight_val[count]
        count += 1
    print(f"计算单牌", p_cards, score)
    return score


# 对子
def calculate_pair(p_cards, score):
    # 排序
    p_cards = sort_list(p_cards)
    card_val = [i[1] for i in p_cards]
    # 去掉重复牌后的牌数(3-1)
    if len(set(card_val)) == 2:
        # 前两张牌是对子
        if card_val[0] == card_val[1]:
            score = (card_val[0] + card_val[1]) * 50 + card_val[2]
        else:
            # 后两张牌是对子
            score = (card_val[2] + card_val[1]) * 50 + card_val[0]
    print(f"计算对子", p_cards, score)
    return score


# 顺子
def calcuate_straight(p_cards, score):
    p_cards = sort_list(p_cards)
    # 提取牌数
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if(b - a == 1 and c - b == 1):
        score *= 100
    print(f"计算顺子", p_cards, score)
    return score


# 同花
def calculate_same_color(p_cards, score):
    # 提取花色
    color_set = {i[0][0] for i in p_cards}
    if len(color_set) == 1:
        score *= 1000
    print(f"计算同花", p_cards, score)
    return score


# 同花顺
def calculate_same_color_straight(p_cards, score):
    p_cards = sort_list(p_cards)
    # 提取牌数
    card_val = [i[1] for i in p_cards]
    a, b, c = card_val
    if(b - a == 1 and c - b == 1):
        color_set = {i[0][0] for i in p_cards}
        if len(color_set) == 1:
            score *= 0.1
        print(f"计算同花顺", p_cards, score)
    return score


# 豹子
def calculate_leopard(p_cards, score):
    # 取出三张牌的值，放进集合去重
    card_val = {i[1] for i in p_cards}
    print(card_val, '11111', len(card_val))
    if len(card_val) == 1:
        score *= 100000
    print(f"计算豹子", p_cards, score)
    return score


""" 4.对比 """
# 将计算分值的函数对象按顺序放到列表中去，遍历列表，传入参数，一次执行判断计算。
calc_func_oders = [
    calculate_Single,
    calculate_pair,
    calcuate_straight,
    calculate_same_color,
    calculate_same_color_straight,
    calculate_leopard
]

# 存放所有玩家的分数
performance = []
for p_name, p_cards in player_dic.items():
    print(f"开始计算玩家{p_name}的牌")
    score = 0
    for calc_func in calc_func_oders:
        score = calc_func(p_cards, score)
    performance.append([p_name, score])

print(performance)
winner = sort_list(performance)[-1]
for i in performance:
    if int(i[1]) == int(winner[1]):
        print("赢家是:", i)