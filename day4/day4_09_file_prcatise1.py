#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day4_09_file_prcatise1.py
@time: 2022/3/1  18:14
# @describe: 2.11 练习题- ⽤户登录认证程序：
    要求⽤户输⼊帐号密码进⾏登陆
    ⽤户账号信息保存在⽂件内
    ⽤户密码输⼊错误三次后锁定⽤户，下次再登录，检测到是这个被锁定的⽤户，则依然不允许其它
    登录，提示已被锁
"""

# accounts = {
#     "alex": ["alex", "abc123!", "1"]
# }

accounts = {}
f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")
    accounts[line[0]] = line
print(accounts)

while True:
    user = input("Username:").strip()
    # 用户未注册
    if user not in accounts:
        print('该用户未注册...')
        continue
    # 1 代表此账户已锁定
    elif accounts[user][2] == '1':
        print('此账户已锁定，请联系管理员...')
        continue
    count = 0
    # 控制密码
    while count < 3:
        passwd = input('Password:').strip()
        # 账号dict 里判断password 对不对
        if passwd == accounts[user][1]:
            print(f'Welcome {user}...登录成功...')
            exit('bye...')
        else:
            print('Wrong password...')
        count += 1

    if count == 3:
        print(f'输错了{count}密码，需要锁定账户{user}...')
        # 1.先改在内存中dict 账号信息的 用户状态
        # 2.把dict 里的数据转车原 account.db 数据格式，并且存回文件
        accounts[user][2] = '1'
        f2 = open('account.db', 'w')
        for user, val in accounts.items():
            # 把列表再转成字符
            line = ",".join(val) + "\n"
            f2.write(line)
        f2.close()
        exit('bye...')
