#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_01_module.py
@time: 2022/3/14  17:28
# @describe: 模块

1.1 什么是模块：
    在计算机程序的开发过程中，随着程序代码越写越多，在⼀个⽂件⾥代码就会越来越⻓，越来越不容易
    维护。
    为了编写可维护的代码，我们把很多代码按功能分组，分别放到不同的⽂件⾥，这样，每个⽂件包含的
    代码就相对较少，很多编程语⾔都采⽤这种组织代码的⽅式。在Python中，⼀个.py⽂件就可以称之为
    ⼀个模块（Module）。

    使⽤模块有什么好处？
        1. 最⼤的好处是⼤⼤提⾼了代码的可维护性。其次，编写代码不必从零开始。当⼀个模块编写完毕，
        就可以被其他地⽅引⽤。我们在编写程序的时候，也经常引⽤其他模块，包括Python内置的模块
        和来⾃第三⽅的模块。
        2. 使⽤模块还可以避免函数名和变量名冲突。每个模块有独⽴的命名空间，因此相同名字的函数和变
        量完全可以分别存在不同的模块中，所以，我们⾃⼰在编写模块时，不必考虑名字会与其他模块冲
        突

    模块分类
    模块分为三种：
        1.内置标准模块（⼜称标准库）执⾏help(‘modules’)查看所有python⾃带模块列表
        2.第三⽅开源模块，可通过pip install 模块名 联⽹安装
        3.⾃定义模块
"""

# 模块导入&调用
"""
# 导入
import module_a
# 导⼊某个模块下的某个⽅法 or ⼦模块
from module import xx 
# 导⼊后⼀个⽅法后重命名
from module.xx.xx import xx as rename
# 导⼊⼀个模块下的所有⽅法，不建议使⽤
from module.xx.xx import *
# 调用
modeule_a.xx
"""

# 自定义模块
"""
创建⼀个.py⽂件，就可以称之为模块，就可以在另外⼀个程序⾥导⼊
"""

# 模块的查找路径
"""
    导⼊⼀个模块时，Python解释器会按照sys.path打印的列表顺序去依次到每个⽬录下去匹配你要导⼊的模块名，
    只要在⼀个⽬录下匹配到了该模块名，就⽴刻导⼊，不再继续往后找。
    ⾃⼰定义的模块在当前⽬录会被优先导⼊
"""
import sys
print(sys.path)


# 第三方开源模块安装
"""
python的开源模块库: https://pypi.python.org/pypi
安装方式：
    1.源码安装：
        下载后，解压并进⼊⽬录，执⾏以下命令完成安装：
            python setup.py build
            python setup.py install
    2.直接通过pip 安装：
        pip install [模块名]
    3.离线安装：
        pip3 install wheel
        pip3 install xxx.whl(文件名称)


"""
