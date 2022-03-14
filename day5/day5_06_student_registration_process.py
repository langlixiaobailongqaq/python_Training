#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day5_06_student_registration_process.py
@time: 2022/3/14  10:01
# @describe: 学籍注册小程序-练习

需求：
    1. 要求⽤户输⼊姓名、年龄、⼿机号、身份证号、所选课程，然后为学员完成注册
    2. ⼿机号、身份证号唯⼀
    3. 可选的课程只能从Python、Linux、⽹络安全、前端、数据分析 这⼏⻔⾥选
    4. 学员信息存⼊⽂件
"""

db_file = 'student_data.db'


def validate_phone(num):
    # 判断是否是数字
    if not num.isdigit():
        exit('手机号必须是数字')
    if len(num) != 11:
        exit('手机号必须达到11位')

    return True


def register_api():
    # 存学员数据
    stu_data = {}
    # center 返回一个原字符串居中, 并使用空格填充至长度width 的新字符串。默认填充字符为空格。
    print('欢迎来到德莱联盟'.center(50, '-'))
    print('请完成学籍注册')
    name = input('姓名:').strip()
    age = input('年龄:').strip()
    phone = input('手机号:').strip()
    if phone in phone_list:
        exit('该手机已注册')
    validate_phone(phone)

    id_num = input('身份证:').strip()
    if id_num in id_num_list:
        print('该身份证号码已注册')

    course_list = ['Python', 'Linux', '⽹络安全', '前端', '数据分析']
    # enumerate，用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在for 循环当中
    for index, course in enumerate(course_list):
        print(f'{index}. {course}')

    selected_course = input('请输入想学的课:')
    if selected_course.isdigit():
        selected_course = int(selected_course)
        # 合法选项
        if selected_course >= 0 and selected_course < len(course_list):
            # 选中的课程
            picked_course = course_list[selected_course]
        else:
            exit('不合法的选项...')
    else:
        exit('非法输入...')

    stu_data['name'] = name
    stu_data['age'] = age
    stu_data['phone'] = phone
    stu_data['id_num'] = id_num
    stu_data['course'] = picked_course
    return stu_data


def commit_to_db(filename, stu_data):
    """
    把学员数据，存到文件里
    :param filename: 学员数据库文件
    :param stu_data: 单个学员数据的dict
    :return:
    """
    f = open(filename, 'a')
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']}," \
          f"{stu_data['id_num']},{stu_data['course']}\n"
    f.write(row)
    f.close()


def load_validated_data(filename):
    f = open(filename)
    phone_list = []
    id_num_list = []
    for line in f:
        line = line.split(',')
        phone = line[2]
        id_num = line[3]
        phone_list.append(phone)
        id_num_list.append(id_num)

    return phone_list, id_num_list


phone_list, id_num_list = load_validated_data(db_file)

student_data = register_api()
print(student_data)
commit_to_db(db_file, student_data)













