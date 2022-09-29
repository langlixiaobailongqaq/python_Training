#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: decorator.py
@time: 2022/9/29  10:22
# @describe: python 装饰器
"""

""" 函数 """


def hi(name='yasuo'):
    return 'hi' + name


print(hi() + '**' * 10)

""" 在函数中定义函数 """


def hi(name='yasuo'):
    print("hi函数")

    def greet():
        return "greet函数"

    def welcome():
        return "welcome函数"

    print(greet())
    print(welcome())
    print("hi函数")


hi()

""" 从函数中返回函数 """


def hi(name='yasuo'):
    def greet():
        return "greet函数" + '**' * 10

    def welcome():
        return "welcome函数"

    if name == 'yasuo':
        return greet
    else:
        return welcome


a = hi()
print(a)

""" 将函数作为参数传给另一个函数 """


def hi():
    return "hi yasuo" + '**' * 10


def doSomethingBeforeHi(func):
    print("1234")
    print(func())


doSomethingBeforeHi(hi)

""" 第一个装饰器 """


def a_new_decorator(a_func):
    def wrapTheFunction():
        print("执行a_func之前")
        a_func()
        print("执行a_func之后"+ '**' * 10)

    return wrapTheFunction


def a_function_requiring_decoration():
    print("a_function_requiring_decoration函数")


a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()


from functools import wraps
def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("@执行a_func之前")
        a_func()
        print("@执行a_func之后" + '**' * 10)
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("@a_function_requiring_decoration")


print(a_function_requiring_decoration.__name__)


""" 装饰器常用场景 """
from functools import wraps
def decorator_name(f):
    """
    注意：@wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
    这可以让我们在装饰器里面访问在装饰之前的函数的属性。
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated

@decorator_name
def func():
    return("Function is running")

can_run = True
print(func())

can_run = False
print(func())



""" 在函数中嵌入装饰器 """
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrappend_function(*args, **kwargs):
            log_string = func.__name__ + 'was called'
            print(log_string)
            # 打开logfile,并写入内容
            with open(logfile, 'a') as opened_file:
                # 将日志达到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrappend_function
    return logging_decorator


@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()



""" 装饰器类 """
from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + 'was called'
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass