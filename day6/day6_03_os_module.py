#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_03_os_module.py
@time: 2022/3/14  18:07
# @describe: 系统调⽤OS模块
    os 模块提供了很多允许你的程序与操作系统直接交互的功能
"""
import os

# 得到当前⼯作⽬录，即当前Python脚本⼯作的⽬录路径:
import signal

print(os.getcwd())

# 返回指定⽬录下的所有⽂件和⽬录名
os.listdir()

# ⽤来删除⼀个⽂件
os.remove()

# 删除多个目录
os.removedirs()

# 检验给出的路径是否是⼀个⽂件
os.path.isfile()

# 检验给出的路径是否是⼀个⽬录
os.path.isdir()

# 判断是否是绝对路径
os.path.isabs()

# 检验给出的路径是否真地存在
os.path.exists()

# 返回⼀个路径的⽬录名和⽂件名
os.path.split()

# 分离路径的扩展名
os.path.splitext()

# 获取路径名
os.path.dirname()

# 获得绝对路径
os.path.abspath()

# 获取文件名
os.path.basename()

# 运行shell 命令
os.system()

# 读取操作系统环境变量HOME的值
os.getenv('HOME')

# 返回操作系统所有的环境变量
os.environ

# 设置系统环境变量，仅程序运⾏时有效
os.environ.setdefault('HOME','/home/alex')

# 返回当前平台使用的行终止符-Windows使⽤'\r\n'，Linux and MAC使⽤'\n'
os.linesep()

# 返回你正在使用的平台-对于Windows，它是'nt'，⽽对于Linux/Unix⽤户，它是'posix'
os.name

# 重命名
# os.rename(old, new)

# 创建多级目录
os.makedirs()

# 创建单个目录
os.mkdir('test')

# 获取文件属性
file, filename, dirname = ''
os.stat(file)

# 修改文件权限与时间戳
os.chmod(file)

# 获取文件大小
os.path.getsize(filename)

# 结合目录名与文件名
os.path.join(dir, filename)

# 改变工作目录到 dirname
os.chdir(dirname)

# 获取当前终端的大小
os.get_terminal_size()

# 杀死进程
os.kill(10884, signal.SIGKILL)