#!/usr/bin/python
# coding=utf-8

"""
用 Python 写一个爬图片的程序，
"""

import os
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlsplit


def catch_pic(url):
    # 打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作。
    html = urllib2.urlopen(url)
    # 利用次文件对象打开url代表的html文件对象
    bs = BeautifulSoup(html, 'lxml')
    # 寻找所有img标签
    for i in bs.find_all('img'):
        # 将img标签里的src属性 也就是图片的网址属性传入
        down_pic(i['src'])


def down_pic(url):
    # 读取图片的地址
    img = urllib2.urlopen(url).read()
    # urlsplit方法将url分成了5个部分   第三个代表的是路径
    file_name = os.path.basename(urlsplit(url)[2])
    output = open(file_name, 'wb')
    output.write(img)
    output.close()

    # with open(file_name,'wb') as f:
    #     f.write(img)


if __name__ == "__main__":
    catch_pic('http://tieba.baidu.com/p/2166231880')
