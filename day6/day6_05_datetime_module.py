#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_05_datetime_module.py
@time: 2022/3/16  15:53
# @describe: datetime 模块
"""
import datetime

"""
    datetime.date：表示日期的类。常用的属性：year、month、day
    datetime.time：表示时间的类。常用属性：hour, minute, second, microsecond
    datetime.datetime：表示日期时间
    datetime.timedelta：表示时间间隔，即两个时间点之间的长度
    datetime.tzinfo：与时区有关的相关信息。
    
"""

"""  1.返回当前的datetime日期类型 """
d = datetime.datetime.now()
print(d, d.timestamp(), d.today(), d.year, d.timetuple())

# 2.时间转换-时间戳转为datetime 日期类型
print(datetime.date.fromtimestamp(1647416960))

# 3.时间运算
d_time = datetime.datetime.now()
# 当前时间 +4天
d_time1 = d_time + datetime.timedelta(4)
print(d_time1)
# 当前时间 +4小时
d_time = d_time + datetime.timedelta(hours=4)
print(d_time)

# 4.时间替换
print(d.replace(year=2999, month=11, day=30))
