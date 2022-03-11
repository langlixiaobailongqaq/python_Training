#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_08_file_practise.py
@time: 2022/3/1  17:32
# @describe: 练习题

    replace()：方法是字符串替换方法，它可将字符串中的部分子串替换成新的部分，并返回新字符串。
    语法：str.replace(old_str, new_str, count)
        old_str：要被替换掉的字符串，string，不可省略的参数
        new_str：使用new_str 替换掉old_str，string，不可省略的参数
        count：最大替换次数，int，可省略的参数

"""

"""
# 练习题-全局⽂本检索替换
需求：
    写⼀个脚本，允许⽤户按以下⽅式执⾏时，即可以对指定⽂件内容进⾏全局替换，且替换完毕后打印替
        换了多少处内容
    写完后的脚本调⽤⽅式：
        python your_script.py old_str new_str filename
        例子： python day4_08_file_practise.py '葫芦娃' '葫芦娃1' staff.txt
"""
import sys


print(sys.argv)
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]

# 1. 加载到内存中
f = open(filename, 'r+')
data = f.read()

# 2.计数和替换
old_str_count = data.count(old_str)
new_data = data.replace(old_str, new_str)

# 3.清除旧文件名
f.seek(0)
f.truncate()

# 4.将新数据保存到文件中
f.write(new_data)
f.close()

print(f''' 成功替换字符'{old_str}' to '{new_str}', 共{old_str_count}处 ''')

