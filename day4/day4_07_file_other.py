#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_07_file_other.py
@time: 2022/3/1  17:11
# @describe: file 其它功能
"""


# 返回⽂件•打开的模式
def mode(self) -> str:
    pass


# 返回⽂件名
def name(self) -> str:
    pass


# 返回⽂件句柄在内核中的索引值，以后做IO多路复⽤时可以⽤到
def fileno(self, *args, **kwargs): # real signature unknown
    pass


# 把⽂件从内存buffer⾥强制刷新到硬盘
def flush(self, *args, **kwargs): # real signature unknown
    pass


# 判断是否可读
def readable(self, *args, **kwargs): # real signature unknown
    pass


# 只读⼀⾏，遇到\r or \n为⽌
def readline(self, *args, **kwargs):  # real signature unknown
    pass


# 把操作⽂件的光标移到指定位置
#     *注意seek的⻓度是按字节算的， 字符编码存每个字符所占的字节⻓度不⼀样。
#     如“路⻜学城” ⽤gbk存是2个字节⼀个字，⽤utf - 8
#     就是3个字节，因此以gbk打开时，
#     seek(4)
#     就把光标切换到了“⻜”和“学”两个字中间。
#     但如果是utf8, seek(4)
#     会导致，拿到了⻜这个字的⼀部分字节，打印的话会报错，因为处理剩
#     下的⽂本时发现⽤utf8处理不了了，因为编码对不上了。少了⼀个字节
def seek(self, *args, **kwargs):  # real signature unknown
    pass


# 判断⽂件是否可进⾏seek操作
def seekable(self, *args, **kwargs): # real signature unknown
    pass


# 返回当前⽂件操作光标位置
def tell(self, *args, **kwargs): # real signature unknown
    pass


# 按指定⻓度截断⽂件
# *指定⻓度的话，就从⽂件开头开始截断指定⻓度，不指定⻓度的话，就从当前位置到⽂件尾部
# 的内容全去掉。
def truncate(self, *args, **kwargs): # real signature unknown
    pass


# 判断⽂件是否可写
def writable(self, *args, **kwargs): # real signature unknown
    pass