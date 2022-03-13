#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_04_return.py
@time: 2022/3/13  11:18
# @describe: 返回值 return

    函数外部的代码要想获取函数的执行结果，就可以在函数里用return 语句把结果返回
    函数在执行过程中只要遇到return 语句，就会停止执行并返回结果，可可以理解为return 语句代表着函数的结束
    如果未在函数中指定return，那么这个函数的返回值为None
"""


def stu_register(name, age, course="Py", country='CN'):
    print('---- 注册学生信息 ---')
    print('姓名:', name)
    print('性别:', age)
    print('国籍:', country)
    print('课程:', course)
    if age > 22:
        return True
    else:
        return False


registriation_status = stu_register('王大鹏', 28, course='Py全栈开发', country='Java')
if registriation_status == True:
    print('注册成功')
else:
    print('注册失败')



