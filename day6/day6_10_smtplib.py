#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_10_smtplib.py
@time: 2022/3/17  13:54
# @describe: 邮件发送smtplib
"""

"""
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是⼀组⽤于由源地址到⽬的地址传送
邮件的规则，由它来控制信件的中转⽅式。

想实现发送邮件需经过以下⼏步：
    1. 登录 邮件服务器
    2. 构造符合邮件协议规则要求的邮件内容 （email模块）
    3. 发送
    
Python对SMTP⽀持有 smtplib 和 email 两个模块， 
 email 负责构造邮件， smtplib 负责发送邮件,它对smtp协议进⾏了简单的封装。
"""

""" 发送⼀封简单的信语法如下 """
import smtplib
# 邮件正文
from email.mime.text import MIMEText
# 邮件头
from email.header import Header


# 登录邮件服务器-服务器地址、端口号
smtp_obj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
# 发件人的邮箱、邮箱密码
smtp_obj.login("xxxx.@qq.com", 'xxxxxxx')

# 设置邮件头信息
msg = MIMEText("人生苦短，我用Python", 'plan', 'utf-8')
# 发送者
msg['From'] = Header('疾风剑豪', 'utf-8')
# 接收者
msg['To'] = Header('德玛西亚', 'utf-8')
# 主题
msg['Subject'] = Header('面对疾风吧', 'utf-8')
# 发送
smtp_obj.sendmail('xxx@qq.com', ['xxxxx@qq.com', '211313xxxxx@qq.com'],
                  msg.as_string())



""" 发送html 格式的邮件 """
# 只需改动 MIMEText() 第2个参数为html
# 设置邮件头信息
mail_body = """ 
            <h5>hello</h5>
            <p>人生苦短，我用Python</P>
            """
msg = MIMEText(mail_body, 'html', 'utf-8')



""" 在html文本中插入图片 """
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header


# 登录邮件服务器
smtp_obj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
smtp_obj.login('xxxxx@qq.com', 'xsxadasxasxa')

# 设置邮件头信息
mail_body = """
            <h5>hello</h5>
            <p>人生苦短，我用Python</P>
            <p><img src="cid:image1"></p>
            """
# 允许添加附件、图片等
msg_root = MIMEMultipart("related")
# 发送者
msg_root['From'] = Header('疾风剑豪', 'utf-8')
# 接收者
msg_root['To'] = Header('德玛西亚', 'utf-8')
# 主题
msg_root['Subject'] = Header('面对疾风吧', 'utf-8')

# 允许添加图片
msgAlternative = MIMEMultipart('alternative')
msgAlternative.attach(MIMEText(mail_body, 'html', 'utf-8'))
# 把邮件正文内容添加到 msg_root 里
msg_root.attach(msgAlternative)

# 加载图片
fp = open('girl.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片ID，在html文本中引用
msgImage.add_header('Content-ID', '<image1>')
# 添加图片到 msg_root 对象里
msg_root.attach(msgImage)

# 发送
smtp_obj.sendmail('xxx@qq.com', ['xxxxx@qq.com', '211313xxxxx@qq.com'],
                  msg_root.as_string())