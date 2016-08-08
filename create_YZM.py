#!/usr/bin/python
# coding=utf-8

"""
使用 Python 生成字母验证码图片
"""
# 从python image library库中导入4个模块，设置字体过滤器，绘图和打开图像
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random
import string

Image_mode = 'RGB'  # 设置图片格式
Image_bg_color = (255, 255, 255)  # 设置底色
Image_Font = 'ariali.ttf'  # 设置绘制的字体
text = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz\
ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))  # 随机产生4个字符 ''.join 的含义是以''为连接字符 返回一个列表
# text = ''.join([random.choice(string.letters) for i in range(4)])

# 生成随机颜色
def randomcolor():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)
    # 不要小括号，自动返回的是包含所有参数的list


#  绘制随机的验证码
def create_identify_code(strs, width=400, height=200, chance=20):
    # 打开一幅图片对象  设置颜色模式 大小与底色
    im = Image.new(Image_mode, (width, height), Image_bg_color)
    # 将图片对象绘制成图片
    draw = ImageDraw.Draw(im)
    # 随机产生噪点
    for x in xrange(width):
        for y in xrange(height):
            if chance < random.randint(1, 100):
                draw.point((x, y), randomcolor())
    # 加载一个实体字体文件
    font = ImageFont.truetype(Image_Font, 80)
    # 注意这里的到的是text的长度  不是单个长度！
    font_width, font_height = font.getsize(text)
    strs_len = len(strs)
    # 设置起始位置
    x = (width - font_width) / 2
    y = (height - font_height) / 2
    for i in strs:
        draw.text((x, y), i, randomcolor(), font)
        x += font_width / strs_len

    im.filter(ImageFilter.BLUR)
    im.save('identifying_code_pic.jpg')


if __name__ == "__main__":
    create_identify_code(text)
