#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_04_time_module.py
@time: 2022/3/16  15:21
# @describe: time 模块
    在Python中，与时间处理有关的模块就包括：
    time，datetime,calendar(很少⽤）
"""
import time

"""
1.对时间的处理：
    时间的显示；
    时间的转换；
    时间的运算
    
2.在python中，通常有以下几种方式来表示时间：
    时间戳(timestamp)：1554864776.161901;
    格式化的时间字符串：2020-10-03 17:54；
    元组(struct_time)：共九个元素-年、月、日、时、分、秒、周(weekday)、⼀年中的第⼏天、是否是夏令时：
        mac环境：time.struct_time(tm_year=2020, tm_mon=4, tm_mday=10, tm_hour=2,
                tm_min=53, tm_sec=15, tm_wday=2, tm_yday=100, tm_isdst=0)
"""

""" time模块的常用方法 """
secs = '1647416960'
# 将一个时间戳转换成当前时区的struct_time。若secs 参数未提供，则以当前时间为准。
print(time.localtime())

# 将一个时间戳转换为UTC 时区(0时区)的struct_time
time.gmtime(secs)

# 返回当前时间的时间戳
time.time()

# 将一个struct_time 转化为时间戳
t = ''
time.mktime(t)

# 线程推迟指定的时间运行，单位：秒
time.sleep(secs)

# 把⼀个代表时间的元组或者struct_time（如由 time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。
# 如果t未指定，将传⼊time.localtime()。
# time.strftime(format[, t])

# 把⼀个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。
# time.strftime(string[, format])
print(time.strptime('2017-10-3 17:54', "%Y-%m-%d %H:%M"))

