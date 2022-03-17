#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:zhengxin
@file: day6_12_prcatise2.py
@time: 2022/3/17  16:17
# @describe: Python生成一千张优秀学员的海报
"""
from PIL import Image, ImageDraw, ImageFont
import qrcode

# 生成一个名字列表
name_list = []
with open('name.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name = line.strip('\n')
        name_list.append(name)
print(name_list)


# 生成二维码函数
def QR_Code(data):
    # 自定义二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=3
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    return img


# 生成优秀学员海报的函数
def xueyuan_name(y_name):
    im_name = Image.open("student.png")
    # 创建画刷
    draw = ImageDraw.Draw(im_name)
    # 设置字体
    font = ImageFont.truetype("/Library/Fonts/Songti.ttc", 30)
    # 写出优秀学员的姓名
    draw.text((220, 310), y_name, fill='#000000', font=font)
    lujin_name = y_name + '.png'

    # 生成二维码，并粘贴在原理二维码位置
    im = QR_Code(lujin_name)
    box = (53, 563, 140, 650)
    im_name.paste(im, box)
    im_name.save(y_name + '.png', 'PNG')


# 生成一千个优秀学员海报图
for l in name_list:
    xueyuan_name(l)