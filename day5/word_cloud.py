#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: word_cloud.py
@time: 2022/3/14  10:57
# @describe: 生成词云
"""
from os.path import join

import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba


text_from_file_with_apath = open('tips.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = ''.join(wordlist_after_jieba)

# 这里的字体路径需要搜索Songti.ttc拷贝)
my_wordcloud = WordCloud(width=1000,\
    font_path="/Library/Fonts/Songti.ttc",\
    height=700).generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()
