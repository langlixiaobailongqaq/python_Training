#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_02_package.py
@time: 2022/3/14  17:53
# @describe: 包(package)
概念：写的项⽬较复杂，有很多代码⽂件的话，为了⽅便管理，可以⽤包来管理。
    ⼀个包其实就是⼀个⽂件⽬录，你可以把属于同⼀个业务线的代码⽂件都放在同⼀个包⾥。
"""

# 创建包
"""
只需要在⽬录下创建⼀个空的 __init__.py ⽂件 ， 这个⽬录就变成了包。这个⽂件叫包的初始化⽂件
，⼀般为空，当然也可以写东⻄，当你调⽤这个包下及其任意⼦包的的任意模块时， 这 个 __init__.py ⽂件都会先执⾏。
注：pycharm，可以直接创建包目录(python package)
"""

# 手动添加sys.path 路径-Pycharm会⾃动添加路径，脱离pycharm执行脚本，会报路径错误
import os
import sys

# 取到主目录路径
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
# 添加到sys.path⾥
sys.path.append(base_dir)
